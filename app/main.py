from fastapi import FastAPI

from app.api.routes_chat import router as chat_router
from app.api.routes_kb import router as kb_router

app = FastAPI(title="HealthBot API", version="0.2.0")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(kb_router, prefix="/kb", tags=["kb"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
