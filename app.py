import streamlit as st
import requests

# Load API key securely from Streamlit Secrets
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
API_KEY = st.secrets["HUGGINGFACE_API_KEY"]  # 🔒 Securely fetch the key

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def query_huggingface(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

# Streamlit UI
st.title("🧠 Epilepsy AI Assistant")
st.write("Ask me anything about epilepsy!")

query = st.text_input("Enter your question:")
if query:
    response = query_huggingface({"inputs": query})
    st.write("**Answer:**", response)
