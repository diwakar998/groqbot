import os
from groq import Groq
import streamlit as st
import pandas as pd
import openpyxl

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_TRACING_V2"]="true"
os.environ["LANGSMITH_API_KEY"]=st.secrets["LangSmith_API"]
os.environ["LANGSMITH_PROJECT"]="test"
from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile"   # or "llama3-70b-8192", etc.
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

client = Groq(api_key=st.secrets["GROQ_API_KEY"],)
# Set the app title
st.set_page_config(page_title="PMO Agent", page_icon="🤖")
st.title("🤖 PMO Agent Chatbot – Ask your question + upload files")

# Add some colored headers
st.markdown("### 🟢 Enter your *PMO* query below:")
#st.text_area("💬 Your Question:", height=100)

input_text=st.text_input("Search the topic u want")
uploaded_file = st.file_uploader(
    "Attach a supporting file (optional)", 
    type=["txt", "pdf", "docx", "csv","xlsx"]
)
# Submit button to control execution
if st.button("Submit"):
    if not input_text:  # Text is mandatory
        st.error("⚠️ Please enter text before submitting.")
    else:
        st.success("✅ Processing your request...")
        #st.write("Text entered:", text_val)    
        if uploaded_file:
            st.write("File uploaded:", uploaded_file.name)
        else:
            st.info("No file uploaded (that’s okay!)")
            
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # Convert to string (you can filter/clean before sending)
    text_data = df.to_string()
else:
    text_data=""

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text+text_data}))

