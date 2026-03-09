from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.ingestion.embedder import embed_text
from app.retrieval.vector_store import VectorStore

text = load_pdf("docs/sample.pdf")

chunks = chunk_text(text)

embeddings = embed_text(chunks)

vector_store = VectorStore(dim=384)
vector_store.add(embeddings, chunks)

print("Documents ingested and indexed successfully.")