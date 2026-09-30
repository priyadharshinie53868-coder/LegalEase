import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "LegalEase API" in data.get("app", "")
    assert data.get("health") == "/health"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "ok"
    assert "healthy" in data.get("message", "")


def test_generate_validation_error_empty_parties():
    payload = {
        "document_type": "NDA",
        "parties": "",
        "terms": "Valid terms for NDA",
        "effective_date": "2026-10-01"
    }
    response = client.post("/generate", json=payload)
    # Pydantic schema validation or endpoint validation
    assert response.status_code in [400, 422]


def test_generate_validation_error_short_terms():
    payload = {
        "document_type": "NDA",
        "parties": "Party A and Party B",
        "terms": "abc",
        "effective_date": "2026-10-01"
    }
    response = client.post("/generate", json=payload)
    assert response.status_code in [400, 422]
