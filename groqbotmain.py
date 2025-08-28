import os
from groq import Groq
import streamlit as st

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)
# Set the app title
st.title("🤖🤖 PMO Groq Reporting & Governance Agent, Your PMO Expert")
# User input
user_input = st.chat_input("How can I help you today...")
#prompt=chatprompttemplate.

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            #"content": "Explain the importance of fast language models",
            "content": user_input,
        }
    ],
    model="llama-3.3-70b-versatile",
)
outvar=chat_completion.choices[0].message.content
st.write(outvar)
print(outvar)
