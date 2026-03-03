from fastapi import FastAPI

from app.api.routes_chat import router as chat_router

app = FastAPI(title="HealthBot API", version="0.0.1")
app.include_router(chat_router)


@app.get("/health")
def health():
    return {"status": "ok"}
