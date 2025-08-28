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
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_TRACING_V2"]="true"
#LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]=st.secrets["LangSmith_API"]
os.environ["LANGSMITH_PROJECT"]="test"
#OPENAI_API_KEY="<your-openai-api-key>"

#LANGCHAIN_TRACING_V2="true"
#LANGCHAIN_API_KEY=st.secrets["LANGCHAIN_API_KEY"]
from langchain_groq import ChatGroq

#llm = ChatGroq()
llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile"   # or "llama3-70b-8192", etc.
)
#llm.invoke("Hello, world!")

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
st.set_page_config(page_title="PMO Agent", page_icon="🤖")
st.title("🤖 PMO Agent Chatbot – Ask your question + upload files")

# Add some colored headers
st.markdown("### 🟢 Enter your *legal* query below:")
st.text_area("💬 Your Question:", height=100)

# Put input + file in columns
col1, col2 = st.columns([2,1])
with col1:
    st.text_input("✍️ Query Header")
with col2:
    st.color_picker("🎨 Pick a highlight color")

uploaded_file = st.file_uploader("📎 Upload Supporting Docs", type=["pdf","docx","txt"])


#st.title("🤖🤖 PMO Groq Reporting & Governance Agent, Your PMO Expert")
# User input
#user_input = st.chat_input("How can I help you today...")
input_text=st.text_input("Search the topic u want")
uploaded_file = st.file_uploader(
    "Attach a supporting file (optional)", 
    type=["txt", "pdf", "docx", "csv"]
)
#prompt=chatprompttemplate.

#chat_completion = client.chat.completions.create(
#    messages=[
#        {
 #           "role": "user",
            #"content": "Explain the importance of fast language models",
  #          "content": input_text,
   #     }
  #  ],
  #  model="llama-3.3-70b-versatile",
#)

output_parser=StrOutputParser()
chain=prompt|llm|output_parser
#chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
#outvar=chat_completion.choices[0].message.content
#st.write(outvar)
#print(outvar)

