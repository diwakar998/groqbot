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

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
