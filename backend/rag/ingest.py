import chromadb

from rag.loader import documents
from rag.splitter import split_text
from rag.embedder import get_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="lenny_transcripts"
)

doc_id = 0

for doc in documents:

    chunks = split_text(doc["content"])

    for chunk in chunks:

        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(doc_id)],
            embeddings=[embedding],
            documents=[chunk]
        )

        doc_id += 1

print("Index Created")
print("Total Chunks:", doc_id)