from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/auth/register", json={
        "username": "test_user",
        "password": "test_pass"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Usuario creado"

def test_register_duplicado():
    # registra el mismo usuario dos veces
    client.post("/auth/register", json={"username": "dupl_user", "password": "pass"})
    response = client.post("/auth/register", json={"username": "dupl_user", "password": "pass"})
    assert response.status_code == 400

def test_login():
    client.post("/auth/register", json={"username": "login_user", "password": "pass123"})
    response = client.post("/auth/login", data={
        "username": "login_user",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_incorrecto():
    response = client.post("/auth/login", data={
        "username": "nadie",
        "password": "mal"
    })
    assert response.status_code == 401