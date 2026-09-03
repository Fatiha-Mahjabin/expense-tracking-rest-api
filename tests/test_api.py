from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense Tracking API is running!"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_unauthorized_expense():
    response = client.post(
        "/expenses/",
        json={
            "title": "Test Lunch",
            "amount": 100,
            "category": "Food"
        }
    )

    assert response.status_code == 401


def test_register_user():
    response = client.post(
        "/users/register",
        json={
            "email": "testuser@example.com",
            "password": "test123456"
        }
    )

    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"


def test_login_user():
    response = client.post(
        "/users/login",
        data={
            "username": "testuser@example.com",
            "password": "test123456"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_create_expense():
    login_response = client.post(
        "/users/login",
        data={
            "username": "testuser@example.com",
            "password": "test123456"
        }
    )

    token = login_response.json()["access_token"]

    response = client.post(
        "/expenses/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Test Dinner",
            "amount": 500,
            "category": "Food"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test Dinner"
    assert data["amount"] == 500
    assert data["category"] == "Food"


def test_get_expenses():
    login_response = client.post(
        "/users/login",
        data={
            "username": "testuser@example.com",
            "password": "test123456"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/expenses/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_expense():
    login_response = client.post(
        "/users/login",
        data={
            "username": "testuser@example.com",
            "password": "test123456"
        }
    )

    token = login_response.json()["access_token"]

    create_response = client.post(
        "/expenses/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Old Dinner",
            "amount": 500,
            "category": "Food"
        }
    )

    expense_id = create_response.json()["id"]

    response = client.put(
        f"/expenses/{expense_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Updated Dinner",
            "amount": 800,
            "category": "Restaurant"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Dinner"
    assert data["amount"] == 800
    assert data["category"] == "Restaurant"


def test_delete_expense():
    login_response = client.post(
        "/users/login",
        data={
            "username": "testuser@example.com",
            "password": "test123456"
        }
    )

    token = login_response.json()["access_token"]

    create_response = client.post(
        "/expenses/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Expense To Delete",
            "amount": 200,
            "category": "Other"
        }
    )

    expense_id = create_response.json()["id"]

    response = client.delete(
        f"/expenses/{expense_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully"
