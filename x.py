import os
import streamlit as st
from fpdf import FPDF

# Sample data (Replace with actual processed_text & query_results from your app)
processed_text = [
    "Source URL: https://example.com\nThis is the extracted content from the website.\n",
    "Source URL: https://another.com\nMore extracted content goes here.\n"
]
query_results = [
    "- **Content:** This is a relevant answer from the documents.\n- **Source URL:** https://example.com\n",
    "- **Content:** Another relevant answer found in the database.\n- **Source URL:** https://another.com\n"
]

# Function to generate a PDF report
def generate_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, "Scheme Research Report", ln=True, align="C")
    pdf.ln(10)

    # Section: Processed URLs and Extracted Content
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, "Processed URLs and Extracted Content", ln=True, align="L")
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    for text in processed_text:
        pdf.multi_cell(0, 8, text)
        pdf.ln(3)

    # Section: User Queries & Relevant Answers
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, "User Queries & Relevant Answers", ln=True, align="L")
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    for result in query_results:
        pdf.multi_cell(0, 8, result)
        pdf.ln(3)

    pdf_filename = "Scheme_Research_Report.pdf"
    pdf.output(pdf_filename)

    return pdf_filename

# Streamlit UI
st.title("Automated Scheme Research Tool")

# Display processed content (For debugging, optional)
st.subheader("Extracted Content")
for text in processed_text:
    st.write(text)

st.subheader("Query Results")
for result in query_results:
    st.write(result)

# Button to generate and download PDF
if st.button("Generate Report"):
    pdf_file = generate_pdf()

    # Read the PDF in binary mode for Streamlit download button
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Click to Download PDF",
        data=pdf_bytes,
        file_name="Scheme_Research_Report.pdf",
        mime="application/pdf"
    )

