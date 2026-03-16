from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest():
    response = client.post(
        "/kb/ingest",
        json={
            "title": "test notes",
            "text": "Drinking water helps hydration. Sleep improves recovery."
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "doc_id" in data
    assert "chunks_added" in data
    assert data["chunks_added"] >= 1
