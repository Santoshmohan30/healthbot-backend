from fastapi import APIRouter

from app.rag.prompts import build_answer
from app.rag.retrieve import retrieve
from app.schemas.chat import ChatRequest, ChatResponse, Source

router = APIRouter()


@router.post("", response_model=ChatResponse)
def chat(req: ChatRequest):
    hits = retrieve(req.question, k=req.top_k)

    sources = []
    for h in hits:
        meta = h["meta"]
        sources.append(
            Source(
                doc_id=meta.get("doc_id", "unknown"),
                title=meta.get("title", "source"),
                chunk_index=int(meta.get("chunk_index", -1)),
                snippet=h["text"][:240],
            )
        )

    answer = build_answer(req.question, hits)
    return ChatResponse(answer=answer, sources=sources)
