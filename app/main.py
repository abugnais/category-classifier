
from fastapi import FastAPI
from app.classifier import CategoryClassifier
from app.models import QueryRequest, BatchRequest, MatchResponse
from app.categories import CATEGORIES

app = FastAPI()

classifier = CategoryClassifier(CATEGORIES)

@app.post("/classify", response_model=list[MatchResponse])
def classify_query(request: QueryRequest):
    matches = classifier.classify(request.query, request.top_n)
    return [{"category": cat, "score": score} for cat, score in matches]

@app.post("/classify/batch", response_model=list[list[MatchResponse]])
def classify_batch(request: BatchRequest):
    batch_results = classifier.classify_batch(request.queries, request.top_n)
    return [
        [{"category": cat, "score": score} for cat, score in result]
        for result in batch_results
    ]
