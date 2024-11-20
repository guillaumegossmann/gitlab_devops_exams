import pytest
from fastapi.testclient import TestClient
from users.main import app

client = TestClient(app)

def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_user():
    response = client.post(
        "/api/users",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_get_user_by_id():
    user_id = 1
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

def test_update_user():
    user_id = 1
    response = client.put(
        f"/api/users/{user_id}",
        json={"email": "updatedemail@example.com"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "updatedemail@example.com"

def test_delete_user():
    user_id = 1
    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 204
