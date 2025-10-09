from llama_cloud_services import LlamaCloudIndex
from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="llama3.1:latest",
    request_timeout=120.0,
    # Manually set the context window to limit memory usage
    context_window=8000,
)

index = LlamaCloudIndex(
  name="rag-project=2",
  project_name="Default",
  organization_id="9-9b47-ed3ccc69652b",
  api_key="llx-",
  llm = llm,
)
query = "What is the price of Modern Wooden Dining Table"
nodes = index.as_retriever().retrieve(query)
response = index.as_query_engine().query(query)