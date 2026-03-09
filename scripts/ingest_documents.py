import os
import sys
import logging
import pickle
import warnings

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

from app.ingestion.loader import load_pdf, load_txt, clean_text
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import embed_text
from app.retrieval.vector_store import VectorStore

text = load_txt("docs/law.txt")
text = clean_text(text)

chunks = chunk_text(text)

print(f"Tổng số chunks: {len(chunks)}")

embeddings = embed_text(chunks)

vector_store = VectorStore(dim=384)
vector_store.add(embeddings, chunks)

with open("vector_store.pkl", "wb") as f:
    pickle.dump(vector_store, f)

print("\nDocuments ingested and indexed successfully.")
print("Vector store saved to vector_store.pkl")