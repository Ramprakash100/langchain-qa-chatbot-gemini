# Enhanced Q&A Chatbot with Google Gemini

An interactive Question & Answer chatbot built using **Python, Streamlit, LangChain, and Google Gemini**. The application allows users to ask questions and receive AI-generated responses through a simple web interface.

## Features

- Interactive chatbot interface using Streamlit
- Google Gemini integration through LangChain
- User-provided Gemini API key
- Configurable temperature and maximum output tokens
- Prompt engineering using `ChatPromptTemplate`
- Response parsing with `StrOutputParser`
- LangSmith tracing and project tracking support

## Tech Stack

- Python
- Streamlit
- LangChain Core
- LangChain Google GenAI
- Google Gemini API
- LangSmith
- Python Dotenv

## Project Structure

```text
langchain-qa-chatbot-gemini/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.10 or a compatible version
- A Google Gemini API key
- An internet connection

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ramprakash100/langchain-qa-chatbot-gemini.git
cd langchain-qa-chatbot-gemini
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API access

Obtain a Gemini API key through Google AI Studio:

[https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

Run the application and enter your API key in the password field in the sidebar. Never commit your actual API key to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to use the chatbot.

## How It Works

1. The user enters a Gemini API key and selects a model.
2. The user submits a question through the Streamlit interface.
3. LangChain formats the question using `ChatPromptTemplate`.
4. `ChatGoogleGenerativeAI` sends the prompt to the selected Gemini model.
5. `StrOutputParser` extracts the response as text.
6. Streamlit displays the generated answer.

## Learning Outcomes

- Integrating Google Gemini with LangChain
- Building LLM-powered applications
- Creating interactive AI interfaces using Streamlit
- Using prompt templates and output parsers
- Configuring model generation parameters
- Exploring LangSmith tracing for LLM applications

## Future Improvements

- Add conversational memory and chat history
- Improve API error handling
- Add support for additional compatible Gemini models
- Improve the user interface and response formatting

## Author

**Ramprakash V.**

GitHub: [https://github.com/Ramprakash100](https://github.com/Ramprakash100)
