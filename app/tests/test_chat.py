from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    client.post(
        "/kb/ingest",
        json={
            "title": "sleep notes",
            "text": "Avoid caffeine late in the day. Keep a consistent sleep schedule."
        },
    )

    response = client.post(
        "/chat",
        json={
            "question": "How can I sleep better?",
            "top_k": 2
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["sources"], list)
