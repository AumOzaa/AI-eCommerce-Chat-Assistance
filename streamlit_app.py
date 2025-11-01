import streamlit as st
import asyncio
from Utilities.agent import agent

st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="centered")
st.title("💬 FurniBot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


# Display previous chat history
for message in st.session_state["chat_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


async def chat(user_input: str):
    response = await agent.run(user_input)
    return response


def run_async(func, *args, **kwargs):
    """Safely run async code inside Streamlit."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(func(*args, **kwargs))


# Handle chat input
if user_input := st.chat_input("Enter your message..."):
    # Add user message
    st.session_state["chat_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate agent response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking..."):
            response = run_async(chat, user_input)
        message_placeholder.markdown(response)

    # Save assistant reply
    st.session_state["chat_history"].append({"role": "assistant", "content": response})
