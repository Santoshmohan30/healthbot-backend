from dataclasses import dataclass
import uuid

from app.rag.chunking import chunk_text
from app.rag.embedder import embed_texts
from app.rag.vectorstore import get_collection

@dataclass
class IngestResult:
    doc_id: str
    chunks_added: int

def ingest_text(title: str, text: str) -> IngestResult:
    collection = get_collection()
    doc_id = str(uuid.uuid4())

    chunks = chunk_text(text)
    if not chunks:
        return IngestResult(doc_id=doc_id, chunks_added=0)

    ids = [f"{doc_id}:{i}" for i in range(len(chunks))]
    embeddings = embed_texts(chunks)
    metadatas = [
        {"doc_id": doc_id, "title": title, "chunk_index": i}
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    return IngestResult(doc_id=doc_id, chunks_added=len(chunks))
