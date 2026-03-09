from app.ingestion.embedder import embed_text


class Retriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query, top_k=5):

        query_embedding = embed_text([query])[0]

        results = self.vector_store.search(query_embedding, top_k)

        return results