# utils/text_extract.py
import PyPDF2
import docx

def extract_text(uploaded_file):
    # Example extraction logic for PDF or DOCX
    if uploaded_file.type == "application/pdf":
        # Extract text from PDF
        return extract_pdf_text(uploaded_file)  # Ensure this is not None or empty
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        # Extract text from DOCX
        return extract_docx_text(uploaded_file)  # Ensure this is not None or empty
    else:
        return ""


def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text
