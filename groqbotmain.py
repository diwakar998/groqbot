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

# Initialize chat history with a health-focused system prompt
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a professional Project management office AI assistant. you are specialized in Agile, TOGAF, Prince2, PMI, PMP, Scrum, Spotify, Lean, Kanban, SixSigma and other project management frameworks"
                "Your role is to help users understand their project status and suggest possible common risk, causes and risk rosolution, root cause analysys"
                "you can provide output in excel, word, charts and other presentable ways if asked by user. show output in tabular format. Give detailed analysis and improvement ideas about the project after project status"
                "If a user asks about anything unrelated to Project management, PMO, Project/program, frameworks, Management, risk, resources, reply: "
                "'I'm here to help with PMO related questions and suggestions. "
                "Please ask about project, program, risks, resources or other PMO related questions/concerns.' "
            )
        }
    ]

# Display all previous messages
#for msg in st.session_state.messages[1:]:  # Skip system prompt in UI
#    with st.chat_message(msg["role"]):
        #st.markdown(msg["content"])

# Create prompt template from the stored messages
prompt = ChatPromptTemplate.from_messages([
    (msg["role"], msg["content"]) for msg in st.session_state.messages] + [
    ("user", "{user_input}")
])

#prompt=ChatPromptTemplate.from_messages(
#    [
#        ("system","You are a helpful assistant. Please response to the user queries"),
#        ("user","Question:{question}")
#    ]
#)

llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile"   # or "llama3-70b-8192", etc.
)

#client = Groq(api_key=st.secrets["GROQ_API_KEY"],)
# Set the app title
st.set_page_config(page_title="AI PMO Agent", page_icon="🤖")
st.title("🤖 PMO AI Agent")

# Add some colored headers
#st.markdown("### 🟢 Hi, How can I help you today !!")
#st.text_area("💬 Your Question:", height=100)

user_input=st.text_input("Hi, How can I help you today ?")

uploaded_file = st.file_uploader(
    "Attach a supporting file (optional)", 
    type=["txt", "pdf", "docx", "csv","xlsx"]
)
# Submit button to control execution
if st.button("Submit"):
    if not user_input:  # Text is mandatory
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
# Process user input
if user_input:
    # Add user's message to history and show
    st.session_state.messages.append({"role": "user", "content": user_input+text_data})
    #with st.chat_message("user")
        #st.markdown(user_input)
        
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if user_input:
    response=chain.invoke({"user_input":user_input})
    st.markdown(response)

