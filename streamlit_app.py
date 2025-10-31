import streamlit as st
import string
import random


def randon_string() -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))

def generating_response() -> str:


def chat_actions():
    st.session_state["chat_history"].append(
        {"role": "user", "content": st.session_state["chat_input"]},
    )

    st.session_state["chat_history"].append(
        {
            "role": "assistant",
            "content": randon_string(),
        },  # This can be replaced with your chat response logic
    )


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


st.chat_input("Enter your message", on_submit=chat_actions, key="chat_input")

for i in st.session_state["chat_history"]:
    with st.chat_message(name=i["role"]):
        st.write(i["content"])
