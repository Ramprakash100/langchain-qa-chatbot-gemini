import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()


#Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot with GENAI"

#Prompt template
prompt=ChatPromptTemplate(
  [
    ("system","You are a helpful assistant, response to the user's queries."),
    ("user","Question:{question}")
  ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    llm = ChatGoogleGenerativeAI(
    model=llm,
    api_key=api_key,
    temperature=temperature,
    max_tokens=max_tokens
    )
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

#Title of the app
st.title("Enhanced Q&A chatbot with GENAI")

##Sidebar settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter Your Gemini API key:",type="password")

##Drop down to select various OpenAI models
llm= st.sidebar.selectbox("Select an gemini model",["gemini-3.7-flash",
                                                    "gemini-3.6-flash",
                                                    "gemini-3.5-flash",
                                                    "gemini-3.5-flash-lite"])

##Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max+_tokens",min_value=50,max_value=1000,value=150)

##Main Interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You: ")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please Enter the query")