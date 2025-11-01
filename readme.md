# AI eCommerce Chat Assistant
This is a project where I built an AI-powered chat assistant for eCommerce use cases.
It can answer questions about products, availability, and details using Ollama, LlamaIndex, and Streamlit.

The goal of this project was to explore how Retrieval-Augmented Generation (RAG) can be used to make chatbots that understand product data.

## Features
- **Interactive Chat Interface** :
    Built with Streamlit, it lets users type and send messages like chatting with a store assistant.

- **AI-Powered Conversations** : Uses Ollama (a local LLM) to generate human-like answers.

- **RAG Integration (Retrieval-Augmented Generation)** : The assistant can refer to local product data through LlamaIndex to give context-based answers.

- **eCommerce-Themed Context** : Can answer questions about furniture, products, and availability (based on sample data).

- **Runs Entirely Offline** : Everything runs locally, no external APIs or internet required once models are set up.

## Installtion
`git clone https://github.com/AumOzaa/AI-eCommerce-Chat-Assistance.git`

`cd AI-eCommerce-Chat-Assistant`

### MacOS/Linux Destro:
Creating a venv :

`python3 -m venv venv`

activate the venv : 

`source venv/bin/activate`

### Windows : 
Creating a venv : 

`python -m venv venv`

Activating the venv :

`venv\Scripts\activate`

### Install requirements  :
`pip install -r requirements.txt`

### Run the project : 
Make sure you have [ollama](https://ollama.com/) installed and running locally before starting the chat.

Make sure you have the mistral nemo model downloaded through ollama.

`ollama run mistral-nemo`

`streamlit run streamlit_app.py`