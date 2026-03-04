from app.rag.embed import embed_texts
from app.rag.ingest import get_collection


def retrieve(question: str, k: int = 4) -> list[dict]:
    col = get_collection()
    q_emb = embed_texts([question])[0]

    res = col.query(
        query_embeddings=[q_emb],
        n_results=k,
        include=["documents", "metadatas", "distances", "ids"],
    )

    hits = []
    for i in range(len(res["ids"][0])):
        hits.append(
            {
                "id": res["ids"][0][i],
                "text": res["documents"][0][i],
                "meta": res["metadatas"][0][i],
                "distance": res["distances"][0][i],
            }
        )
    return hits
