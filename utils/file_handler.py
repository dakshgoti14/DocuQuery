import pdfplumber
from docx import Document

def extract_text_from_file(file, file_type):
    print(file_type)
    if file_type == "pdf":
        return extract_text_from_pdf(file)
    elif file_type == "docx":
        return extract_text_from_docx(file)
    elif file_type == "txt":
        return extract_text_from_txt(file)
    else:
        raise ValueError("Unsupported file type.")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_text_from_docx(file):
    doc = Document(file)
    full_text = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
    return "\n".join(full_text).strip()

def extract_text_from_txt(file):
    return file.read().decode("utf-8").strip()
