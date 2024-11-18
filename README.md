# Chat Bot with Ollama Integration

A Streamlit-based chat interface for interacting with local Ollama models.

## Features

- Chat with any locally installed Ollama model
- Select from available models through a dropdown menu
- Clean and intuitive user interface
- Chat history with message persistence
- Clear chat functionality

## Prerequisites

1. Python 3.7 or higher
2. Ollama installed and running locally
3. At least one model installed in Ollama

## Installation

1. Clone the repository:
```bash
git clone https://github.com/learnbydoingwithsteventest/chat_bot.git
cd chat_bot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure Ollama is running locally
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and navigate to the provided URL (typically http://localhost:8501)
4. Select a model from the dropdown menu in the sidebar
5. Start chatting!

## Note

Ensure that you have at least one model installed in Ollama. You can install models using:
```bash
ollama pull modelname
```

For example:
```bash
ollama pull llama2
