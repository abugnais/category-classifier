
from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    query: str
    top_n: int = 1

class BatchRequest(BaseModel):
    queries: List[str]
    top_n: int = 1

class MatchResponse(BaseModel):
    category: str
    score: float
