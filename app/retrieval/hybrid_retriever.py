class HybridRetriever:
    def __init__(self, vector_retriever, keyword_retriever):
        self.vector = vector_retriever
        self.keyword = keyword_retriever

    def retrieve(self, query, top_k=5):
        vector_results = self.vector.retrieve(query, top_k)
        keyword_results = self.keyword.search(query, top_k)

        # Combine and deduplicate results
        combined =  vector_results + keyword_results
        return combined