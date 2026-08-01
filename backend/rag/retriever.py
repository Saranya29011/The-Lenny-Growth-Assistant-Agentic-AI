import chromadb

from rag.embedder import get_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "lenny_transcripts"
)

def retrieve_context(query):

    embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=5
    )

    return "\n\n".join(
        results["documents"][0]
    )