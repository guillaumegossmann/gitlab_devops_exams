import pytest
from fastapi.testclient import TestClient
from orders.main import app

client = TestClient(app)

def test_get_orders():
    response = client.get("/api/orders")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_order():
    response = client.post(
        "/api/orders",
        json={
            "product_id": 123,
            "quantity": 2,
            "price": 99.99
        }
    )
    assert response.status_code == 201
    assert response.json()["product_id"] == 123

def test_get_order_by_id():
    order_id = 1
    response = client.get(f"/api/orders/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_delete_order():
    order_id = 1
    response = client.delete(f"/api/orders/{order_id}")
    assert response.status_code == 204
