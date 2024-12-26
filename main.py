import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai
import pickle
import os
from configparser import ConfigParser

# Load OpenAI API Key from config file
config = ConfigParser()
config.read(".config")
openai.api_key = config.get("openai", "api_key")

# Initialize Streamlit App
st.set_page_config(page_title="Automated Scheme Research Tool", layout="wide")
st.title("Automated Scheme Research Tool")

# Sidebar Inputs
st.sidebar.header("Input URLs")
url_input = st.sidebar.text_area("Enter URLs (one per line):", placeholder="Paste your article URLs here, one per line")
process_button = st.sidebar.button("Process URLs")

st.sidebar.header("Ask Questions")
query = st.sidebar.text_input("Enter your question:", placeholder="What are the scheme benefits?")
ask_button = st.sidebar.button("Ask Question")

# File to store FAISS index
INDEX_FILE = "faiss_store_openai.pkl"

# Helper function to load or create FAISS index
def load_or_create_faiss_index():
    """Load existing FAISS index or return None if not available."""
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "rb") as file:
            return pickle.load(file)
    return None

faiss_index = load_or_create_faiss_index()

# Processing URLs
if process_button:
    if not url_input.strip():
        st.error("Please enter at least one URL.")
    else:
        try:
            # Load articles from URLs
            urls = [url.strip() for url in url_input.split("\n") if url.strip()]
            st.info(f"Processing {len(urls)} URLs...")
            loader = UnstructuredURLLoader(urls)
            docs = loader.load()
            st.success(f"Successfully loaded {len(docs)} articles!")

            # Split articles into manageable chunks
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
            texts = text_splitter.split_documents(docs)

            # Generate embeddings and create FAISS index
            embeddings = OpenAIEmbeddings()
            faiss_index = FAISS.from_documents(texts, embeddings)

            # Save FAISS index
            with open(INDEX_FILE, "wb") as file:
                pickle.dump(faiss_index, file)
            st.success("FAISS index created and saved locally!")
        except Exception as e:
            st.error(f"An error occurred during processing: {str(e)}")

# Querying the FAISS index
if ask_button:
    if not faiss_index:
        st.warning("No FAISS index found. Please process URLs first.")
    elif not query.strip():
        st.error("Please enter a question.")
    else:
        try:
            # Perform similarity search
            results = faiss_index.similarity_search(query, k=3)
            st.write("### Relevant Results:")
            for idx, doc in enumerate(results):
                st.write(f"**Result {idx + 1}:**")
                st.write(f"- **Content:** {doc.page_content}")
                st.write(f"- **Source URL:** {doc.metadata.get('source', 'N/A')}")
                st.markdown("---")
        except Exception as e:
            st.error(f"An error occurred while querying: {str(e)}")

# Display a warning if no FAISS index exists
if not faiss_index and not process_button:
    st.warning("No FAISS index found. Please process URLs first.")
