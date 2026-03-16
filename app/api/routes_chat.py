from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse, Source
from app.services.answer_service import build_debug_answer
from app.services.retrieval_service import retrieve_text

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("", response_model=ChatResponse)
def chat(req: ChatRequest):
    hits = retrieve_text(req.question, req.top_k)
    answer = build_debug_answer(req.question, hits)

    sources = []
    for hit in hits:
        meta = hit["meta"] or {}
        sources.append(
            Source(
                doc_id=meta.get("doc_id", "unknown"),
                title=meta.get("title", "unknown"),
                chunk_index=meta.get("chunk_index", -1),
                snippet=hit["text"][:300],
            )
        )

    return ChatResponse(answer=answer, sources=sources)
