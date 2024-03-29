from fastapi.testclient import TestClient  # requests
from main import app

client = TestClient(app)


def test_entries_list():
    response = client.get("/entries/")
    # requests.get()
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_entries_create():
    response = client.post("/entries/", json={"title": "hello"})
    assert response.status_code == 201
    # assert len(response.json().keys()) == 2

def test_entries_create_invalid():
    response = client.post("/entries/", json={"content": "hello"})
    assert response.status_code == 422