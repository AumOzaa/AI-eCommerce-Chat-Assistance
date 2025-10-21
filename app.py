import os
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.memory import ChatMemoryBuffer
import streamlit as st

load_dotenv()


model = Ollama(
    model = os.getenv("MODEL"),
    request_timeout=120.0,
    context_window=8000
)

Settings.embed_model = HuggingFaceEmbedding(model_name=os.getenv("HF_EMBED_MODEL"))

documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(
    documents,
    # we can optionally override the embed_model here
    # embed_model=Settings.embed_model,
)

memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

chat_engine = index.as_chat_engine(
    llm = model,
    chat_mode="context",
    memory=memory,
    system_prompt = (
    "You are a helpful and friendly shopping assistant chatbot. "
),
)

while True:
    userIn = input("User : ")
    if userIn.lower() == '/bye':
        break
    print(chat_engine.chat(userIn).response)
