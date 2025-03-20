import streamlit as st
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from sentence_transformers import SentenceTransformer

# Load Hugging Face embeddings (FREE)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load ChromaDB
vectorstore = Chroma(persist_directory="./chromadb", embedding_function=embedding_model.encode)

# Set up QA system
qa_chain = RetrievalQA.from_chain_type(llm="gpt-3.5-turbo", retriever=vectorstore.as_retriever())

# Streamlit UI
st.title("🧠 Epilepsy AI Assistant")
st.write("Ask me anything about epilepsy!")

# User input
query = st.text_input("Enter your question:")
if query:
    response = qa_chain.run(query)
    st.write("**Answer:**", response)