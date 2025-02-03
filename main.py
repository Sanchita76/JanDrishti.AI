import os
import io
import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai
from dotenv import load_dotenv
from fpdf import FPDF

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is missing. Please set OPENAI_API_KEY in .env file.")
openai.api_key = openai_api_key

# Initialize Streamlit App
st.set_page_config(page_title="JanDrishti", layout="wide")
st.title("JanDrishti - Citizens' Scheme Research Application 👩‍👩‍👧‍👦")

# Sidebar for URL input
st.sidebar.header("Input URLs to Search 📲")
url_input = st.sidebar.text_area("Enter URLs (one per line):↩️")
uploaded_file = st.sidebar.file_uploader("Upload a .txt file with URLs 📤", type=["txt"])
process_button = st.sidebar.button("Process URLs ✅")

# Sidebar for querying
st.sidebar.header("Ask Questions❔❔")
query = st.sidebar.text_input("Enter your question:✍🏾✍🏾")
ask_button = st.sidebar.button("Ask Question ⏩")

# Load FAISS Index if exists
if os.path.exists("faiss_store"):
    faiss_index = FAISS.load_local("faiss_store", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
else:
    faiss_index = None

# Persistent session state for storing processed data
if "processed_text" not in st.session_state:
    st.session_state.processed_text = []
if "query_results" not in st.session_state:
    st.session_state.query_results = []

# Process URLs
if process_button:
    try:
        urls = []

        if url_input.strip():
            urls.extend(url_input.strip().split("\n"))

        if uploaded_file:
            file_content = uploaded_file.read().decode("utf-8")
            file_urls = file_content.strip().split("\n")
            urls.extend(file_urls)

        if not urls:
            st.error("Please enter URLs manually or upload a .txt file.✍🏾 📝")
        else:
            loader = UnstructuredURLLoader(urls)
            docs = loader.load()
            st.success("Articles successfully loaded! ⌛️📜")

            for doc in docs:
                st.session_state.processed_text.append(f"Source URL: {doc.metadata.get('source', 'N/A')}\n{doc.page_content}\n\n")

            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
            texts = text_splitter.split_documents(docs)

            embeddings = OpenAIEmbeddings()
            faiss_index = FAISS.from_documents(texts, embeddings)
            faiss_index.save_local("faiss_store")
            st.success("URLs processed and FAISS index created! ⏰✅")
    except Exception as e:
        st.error(f"Error processing URLs: {str(e)}")

# Ask a question
if ask_button and faiss_index:
    try:
        if not query.strip():
            st.error("Please enter a question.❗️❗️")
        else:
            docs = faiss_index.similarity_search(query, k=3)
            st.write("### Relevant Answers Found!: 📰")
            for doc in docs:
                result = f"- Content: {doc.page_content}\n- Source URL: {doc.metadata.get('source', 'N/A')}\n"
                st.session_state.query_results.append(result)
                st.write(result)
            st.markdown("---")
    except Exception as e:
        st.error(f"Error retrieving answers: {str(e)}")

# Ensure FAISS index is available
if not faiss_index:
    st.warning("No FAISS index found. Please process URLs first.🚫")

# Generate PDF function
def generate_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)  # Reduce bottom margin for more content per page
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", style='B', size=14)  # Use Helvetica for a clean look
    pdf.cell(200, 8, "Scheme Research Report", ln=True, align="C")
    pdf.ln(5)

    # Section: Processed Content
    pdf.set_font("Helvetica", style='B', size=10)
    pdf.cell(200, 6, "Processed URLs and Extracted Content", ln=True, align="L")
    pdf.ln(3)  # Reduced line spacing

    pdf.set_font("Helvetica", size=9)  # Reduce font size for compact content
    if st.session_state.processed_text:
        for text in st.session_state.processed_text:
            pdf.multi_cell(0, 5, text.encode('latin1', 'replace').decode('latin1'))  # Reduce cell height
            pdf.ln(2)  # Reduced spacing between paragraphs
    else:
        pdf.cell(200, 6, "No processed content available.", ln=True, align="L")

    # Section: Query Results
    pdf.set_font("Helvetica", style='B', size=10)
    pdf.cell(200, 6, "User Queries & Relevant Answers", ln=True, align="L")
    pdf.ln(3)

    pdf.set_font("Helvetica", size=9)
    if st.session_state.query_results:
        for result in st.session_state.query_results:
            pdf.multi_cell(0, 5, result.encode('latin1', 'replace').decode('latin1'))  # Reduce cell height
            pdf.ln(0)  # Reduce spacing between answers
    else:
        pdf.cell(200, 6, "No relevant answers found.", ln=True, align="L")

    pdf_filename = "Scheme_Research_Report.pdf"
    pdf.output(pdf_filename, "F")  # Save PDF
    return pdf_filename

# Display Extracted Content
st.subheader("Extracted Documentation about Scheme 📂")
for text in st.session_state.processed_text:
    st.write(text)

#st.subheader("Query Results")
#for result in st.session_state.query_results:
    #st.write(result)

# Show "Generate Report" only when data exists
if st.session_state.processed_text and st.session_state.query_results:
    if st.button("Generate Detailed Report 📜📜"):
        pdf_file = generate_pdf()

        # Ensure PDF is successfully created before showing download button
        if os.path.exists(pdf_file):
            with open(pdf_file, "rb") as f:
                pdf_bytes = f.read()

            st.download_button(
                label="Click to Download PDF 📳",
                data=pdf_bytes,
                file_name="Scheme_Research_Report.pdf",
                mime="application/pdf"
            )
else:
    st.warning("Process URLs and ask a question before generating a report.")
