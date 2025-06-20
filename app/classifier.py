
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CategoryClassifier:
    def __init__(self, categories: dict[str, str], model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.category_names = list(categories.keys())
        self.category_embeddings = self.model.encode(list(categories.values()))

    def classify(self, query: str, top_n: int = 1):
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.category_embeddings)[0]
        top_indices = np.argsort(similarities)[::-1][:top_n]
        return [(self.category_names[i], float(similarities[i])) for i in top_indices]

    def classify_batch(self, queries: list[str], top_n: int = 1):
        query_embeddings = self.model.encode(queries)
        results = []
        for emb in query_embeddings:
            similarities = cosine_similarity([emb], self.category_embeddings)[0]
            top_indices = np.argsort(similarities)[::-1][:top_n]
            results.append([(self.category_names[i], float(similarities[i])) for i in top_indices])
        return results
