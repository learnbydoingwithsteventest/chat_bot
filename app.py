import streamlit as st
import requests
import json

# Set page config
st.set_page_config(page_title="Chat with Ollama", page_icon="🤖", layout="wide")

# Initialize session state for messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_available_models():
    """Fetch available models from Ollama"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = [model["name"] for model in response.json()["models"]]
            return models
        return []
    except:
        return []

def generate_response(prompt, model):
    """Generate response from Ollama"""
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return "Error: Failed to get response from the model."
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar for model selection
st.sidebar.title("Chat Settings")
available_models = get_available_models()

if not available_models:
    st.sidebar.error("No models found. Please make sure Ollama is running and has models installed.")
    model = None
else:
    model = st.sidebar.selectbox("Select Model", available_models)
    st.sidebar.markdown("""
    ### How to use:
    1. Select a model from the dropdown
    2. Type your message in the chat input
    3. Press Enter or click Send to chat
    
    ### Available Models:
    """)
    for m in available_models:
        st.sidebar.markdown(f"- {m}")

# Main chat interface
st.title("Chat with Ollama 🤖")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    if not model:
        st.error("Please select a model first.")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, model)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# Add a clear button to reset the chat
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
