from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking on langsmith dashboard
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful chatbot assistant. Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API and Langsmith Dashboard')
your_input=st.text_input("Ask your query to Bot")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo-16k-0613")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if your_input:
    st.write(chain.invoke({'question':your_input}))
