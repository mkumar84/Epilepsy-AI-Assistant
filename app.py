import streamlit as st
from transformers import pipeline

# Load a FREE LLM from Hugging Face
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

# Initialize model
model = load_model()

# Streamlit UI
st.title("🧠 Epilepsy AI Assistant")
st.write("Ask me anything about epilepsy!")

# User input
query = st.text_input("Enter your question:")
if query:
    response = model(query, max_length=200, do_sample=True)
    st.write("**Answer:**", response[0]["generated_text"])
