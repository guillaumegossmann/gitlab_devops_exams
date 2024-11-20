import pytest
from fastapi.testclient import TestClient
from gateway.main import app

client = TestClient(app)

def test_login_success():
    response = client.post(
        "/api/login",
        json={"username": "admin", "password": "a"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    response = client.post(
        "/api/login",
        json={"username": "admin", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_get_users_admin():
    # Remplacez *** par un token JWT valide pour admin
    token = "Bearer ***"
    response = client.get(
        "/api/users",
        headers={"Authorization": token}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    # Remplacez *** par un token JWT valide pour admin
    token = "Bearer ***"
    response = client.post(
        "/api/users",
        headers={"Authorization": token},
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "securepass"
        }
    )
    assert response.status_code == 201
    assert response.json()["username"] == "newuser"
