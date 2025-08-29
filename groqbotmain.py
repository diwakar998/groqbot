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
#LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]=st.secrets["LangSmith_API"]
os.environ["LANGSMITH_PROJECT"]="test"
#OPENAI_API_KEY="<your-openai-api-key>"
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

client = Groq(api_key=st.secrets["GROQ_API_KEY"],)
# Set the app title
st.set_page_config(page_title="PMO Agent", page_icon="🤖")
st.title("🤖 PMO Agent Chatbot – Ask your question + upload files")

# Add some colored headers
st.markdown("### 🟢 Enter your *PMO* query below:")
#st.text_area("💬 Your Question:", height=100)

#uploaded_file = st.file_uploader("📎 Upload Supporting Docs", type=["pdf","docx","txt"])

#st.title("🤖🤖 PMO Groq Reporting & Governance Agent, Your PMO Expert")
# User input
#user_input = st.chat_input("How can I help you today...")
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
else
    text_data=""
    #prompt=chatprompttemplate.
    #st.write(text_data)
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
    st.write(chain.invoke({"question":input_text+text_data}))
#outvar=chat_completion.choices[0].message.content
#st.write(outvar)
#print(outvar)

