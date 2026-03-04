from fastapi import APIRouter

from app.rag.ingest import ingest_text
from app.schemas.kb import IngestRequest, IngestResponse

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest(req: IngestRequest):
    result = ingest_text(title=req.title, text=req.text)
    return IngestResponse(doc_id=result.doc_id, chunks_added=result.chunks_added)
