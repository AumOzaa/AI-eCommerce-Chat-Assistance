from Utilities.agent import agent
import asyncio
import streamlit as st

async def get_response(user_input):
    return await agent.run(user_input)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: #fafafa;
        }
        .stTextInput > div > div > input {
            background-color: #262730;
            color: white;
            border-radius: 8px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
        }
        .stMarkdown {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🤖 AI Chatbot")
st.markdown("Ask anything about your data — powered by Ollama + LlamaIndex ⚡")

user_input = st.text_input("Type your message:")

# Button click event
if st.button("Ask"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            try:
                response = asyncio.run(get_response(user_input))
                st.markdown(f"**You:** {user_input}")
                st.markdown(f"**Bot:** {response}")
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("Please enter a message first.")

# async def chat():
#     while True:
#         user_input = input("You : ")
#         output = await agent.run(user_input)
#         print("Agent :", output)

# asyncio.run(chat())
