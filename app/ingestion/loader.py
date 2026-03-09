import re
from pypdf import PdfReader

def clean_text(text: str) -> str:
    text = re.sub(r'[ \t]+', ' ', text)       # nhiều space/tab -> 1 space
    text = re.sub(r' *\n *', '\n', text)      # xóa space thừa quanh newline
    text = re.sub(r'\n{3,}', '\n\n', text)   # nhiều dòng trống -> tối đa 2
    return text.strip()

def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()