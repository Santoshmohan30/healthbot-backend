from fastapi import FastAPI

from app.api.routes_chat import router as chat_router
from app.api.routes_health import router as health_router
from app.api.routes_kb import router as kb_router

app = FastAPI(title="HealthBot Backend", version="1.0.0")

app.include_router(health_router)
app.include_router(kb_router)
app.include_router(chat_router)
