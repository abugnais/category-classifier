
# Category Classifier API

A FastAPI-based microservice that classifies text queries (e.g., user search terms) into high-level categories like "clothes", "electronics", etc., using local sentence embeddings.

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t category-classifier .
docker run -p 8000:8000 category-classifier
```

## 📦 API Endpoints

- `POST /classify`: Single query
- `POST /classify/batch`: Multiple queries

## 📚 Example

```bash
curl -X POST http://localhost:8000/classify -H "Content-Type: application/json" -d '{"query": "red hoodie", "top_n": 2}'
```

## 🧠 Powered by

- [FastAPI](https://fastapi.tiangolo.com/)
- [SentenceTransformers](https://www.sbert.net/)
