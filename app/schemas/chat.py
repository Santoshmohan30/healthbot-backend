from typing import List

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)
    top_k: int = Field(default=4, ge=1, le=10)


class Source(BaseModel):
    doc_id: str
    title: str
    chunk_index: int
    snippet: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
