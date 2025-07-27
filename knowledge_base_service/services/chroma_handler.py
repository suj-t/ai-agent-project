import chromadb
from chromadb.utils import embedding_functions
from services.embedder import get_embedding
import os

client = chromadb.Client()
collection = client.get_or_create_collection("knowledge_base")

def ingest_documents():
    try:
        docs_dir = "data/docs"
        for filename in os.listdir(docs_dir):
            with open(os.path.join(docs_dir, filename), "r") as f:
                content = f.read()
                embedding = get_embedding(content)
                collection.add(
                    documents=[content],
                    embeddings=[embedding],
                    ids=[filename]
                )
        return True
    except Exception as e:
        print(f"Ingest error: {e}")
        return False

def query_documents(query_text):
    try:
        query_embedding = get_embedding(query_text)
        results = collection.query(query_embeddings=[query_embedding], n_results=1)
        return results['documents'][0][0] if results['documents'] else "No match found"
    except Exception as e:
        print(f"Query error: {e}")
        return "Error in search"
