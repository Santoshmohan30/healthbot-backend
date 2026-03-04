from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    title: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


class IngestResponse(BaseModel):
    doc_id: str
    chunks_added: int
