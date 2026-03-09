from rank_bm25 import BM25Okapi

class KeywordSearch:
    def __init__(self, documents):
        self.docs = documents
        tokenized = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(tokenized)


    def search(self, query: str, top_k = 5):
        scores = self.bm25.get_scores(query.split())
        
        ranked = sorted(
            range(len(scores)),
            key=lambda i: scores[i], 
            reverse=True
            )
    
        return [self.docs[i] for i in ranked[:top_k]]