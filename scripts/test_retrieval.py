import pickle
from app.ingestion.embedder import embed_texts

# load vector store
with open("vector_store.pkl", "rb") as f:
    vector_store = pickle.load(f)

query = "Chế độ lưu giữ tài liệu của doanh nghiệp"

query_embedding = embed_texts([query])

results = vector_store.search(query_embedding, top_k=5)

for i, r in enumerate(results):
    print("------")
    print(r[:200])