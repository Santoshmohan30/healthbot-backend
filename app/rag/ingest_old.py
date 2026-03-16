import os
import uuid
from dataclasses import dataclass

import chromadb
from chromadb.config import Settings

from app.rag.embed import embed_texts

CHROMA_DIR = os.path.join("data", "chroma")
COLLECTION_NAME = "healthbot_kb"


def get_collection():
    client = chromadb.PersistentClient(
        path=CHROMA_DIR,
        settings=Settings(anonymized_telemetry=False),
    )
    return client.get_or_create_collection(name=COLLECTION_NAME)


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120) -> list[str]:
    text = text.strip()
    if not text:
        return []
    chunks: list[str] = []
    i = 0
    while i < len(text):
        j = min(len(text), i + chunk_size)
        chunks.append(text[i:j])
        i = max(j - overlap, j)
    return chunks


@dataclass
class IngestResult:
    doc_id: str
    chunks_added: int


def ingest_text(title: str, text: str) -> IngestResult:
    col = get_collection()

    doc_id = str(uuid.uuid4())
    chunks = chunk_text(text)
    if not chunks:
        return IngestResult(doc_id=doc_id, chunks_added=0)

    ids = [f"{doc_id}:{k}" for k in range(len(chunks))]
    embeddings = embed_texts(chunks)
    metadatas = [
        {"doc_id": doc_id, "title": title, "chunk_index": k} for k in range(len(chunks))
    ]

    col.add(ids=ids, documents=chunks, embeddings=embeddings, metadatas=metadatas)
    return IngestResult(doc_id=doc_id, chunks_added=len(chunks))
