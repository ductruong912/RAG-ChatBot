from sentence_transformers import SentenceTransformer

model = SentenceTransformer('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, documents, top_k=5):
    pairs = [[query, doc] for doc in documents]
    scores = model.predict(pairs)

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked[:top_k]]