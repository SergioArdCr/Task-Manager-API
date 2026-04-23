# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

def test_register(client):
    response = client.post("/auth/register", json={
        "username": "test_user",
        "password": "1234",
        "rol": "admin"
    })
    assert response.status_code == 200

def test_register_duplicado(client):
    client.post("/auth/register", json={"username": "dupl_user", "password": "1234"})
    response = client.post("/auth/register", json={"username": "dupl_user", "password": "1234"})
    assert response.status_code == 400

def test_login(client):
    client.post("/auth/register", json={"username": "login_user", "password": "1234"})
    response = client.post("/auth/login", data={"username": "login_user", "password": "1234"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_incorrecto(client):
    response = client.post("/auth/login", data={"username": "nadie", "password": "mal"})
    assert response.status_code == 401