from fastapi import APIRouter

from app.schemas.kb import IngestRequest, IngestResponse
from app.services.ingest_service import ingest_text

router = APIRouter(prefix="/kb", tags=["kb"])

@router.post("/ingest", response_model=IngestResponse)
def ingest(req: IngestRequest):
    result = ingest_text(req.title, req.text)
    return IngestResponse(doc_id=result.doc_id, chunks_added=result.chunks_added)
