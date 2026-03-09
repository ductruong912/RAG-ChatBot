from pypdf import pdfReader

def load_pdf(file_path: str):

    reader = pdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text