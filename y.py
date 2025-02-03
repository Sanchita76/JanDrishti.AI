import os
import streamlit as st
from fpdf import FPDF

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Scheme Research Report", ln=True, align="C")

    pdf_filename = "Scheme_Research_Report.pdf"
    pdf.output(pdf_filename)

    # Check if file exists after saving
    if os.path.exists(pdf_filename):
        st.success(f"PDF successfully generated at {os.path.abspath(pdf_filename)}")
    else:
        st.error("PDF generation failed!")

    return pdf_filename

if st.button("Generate Report"):
    pdf_file = generate_pdf()

if os.path.exists("Scheme_Research_Report.pdf"):
    with open("Scheme_Research_Report.pdf", "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Click to Download PDF",
        data=pdf_bytes,
        file_name="Scheme_Research_Report.pdf",
        mime="application/pdf"
    )
else:
    st.error("PDF file not found! Please generate it first.")
