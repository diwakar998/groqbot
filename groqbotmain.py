import os
from groq import Groq
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_community.llms import groq
#import streamlit as st
#import os
#from dotenv import load_dotenv
LANGSMITH_TRACING="true"
LANGSMITH_TRACING_V2="true"
#LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY=st.secrets["LangSmith_API"]
LANGSMITH_PROJECT="test"
#OPENAI_API_KEY="<your-openai-api-key>"

#LANGCHAIN_TRACING_V2="true"
#LANGCHAIN_API_KEY=st.secrets["LANGCHAIN_API_KEY"]
from langchain_groq import ChatGroq

#llm = ChatGroq()
llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile"   # or "llama3-70b-8192", etc.
)
llm.invoke("Hello, world!")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)
# Set the app title
st.title("🤖🤖 PMO Groq Reporting & Governance Agent, Your PMO Expert")
# User input
#user_input = st.chat_input("How can I help you today...")
input_text=st.text_input("Search the topic u want")
#prompt=chatprompttemplate.

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            #"content": "Explain the importance of fast language models",
            "content": input_text,
        }
    ],
    model="llama-3.3-70b-versatile",
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
outvar=chat_completion.choices[0].message.content
st.write(outvar)
#print(outvar)

