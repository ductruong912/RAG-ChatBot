import re

def chunk_text(text: str) -> list[str]:
    parts = re.split(r'(?=Điều \d+\.)', text)
    chunks = [p.strip() for p in parts if p.strip()]
    return chunks