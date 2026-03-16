from app.rag.embedder import embed_texts
from app.rag.vectorstore import get_collection

def retrieve_text(question: str, top_k: int = 4) -> list[dict]:
    collection = get_collection()
    query_embedding = embed_texts([question])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    ids = results.get("ids", [[]])[0]
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for i in range(len(ids)):
        hits.append(
            {
                "id": ids[i],
                "text": docs[i] if i < len(docs) else "",
                "meta": metas[i] if i < len(metas) else {},
                "distance": distances[i] if i < len(distances) else None,
            }
        )

    return hits
