import requests

endpoint = "https://johnnymacaroni.ru/entries/"


client = requests


def test_entries_list():
    response = client.get(endpoint)
    # requests.get()
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_entries_create():
    #response = client.post(endpoint, json={"title": "hello"})
    response = client.post(endpoint, json={"title": "TITLE", "content": "CONTENT"})
    print(response.json())
    assert response.status_code == 201
    # assert len(response.json().keys()) == 2

def test_entries_create_invalid():
    response = client.post(endpoint, json={"content": "hello"})
    assert response.status_code == 422

if __name__ == "__main__":
    test_entries_create()