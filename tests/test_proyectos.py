from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token(username="proj_user"):
    client.post("/auth/register", json={"username": username, "password": "1234"})
    response = client.post("/auth/login", data={"username": username, "password": "1234"})
    return response.json()["access_token"]

def test_crear_proyecto():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/proyectos/", json={
        "nombre": "Test Proyecto",
        "descripcion": "Descripción"
    }, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_proyectos():
    token = get_token("proj_user2")
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/proyectos/", json={"nombre": "P1", "descripcion": "D1"}, headers=headers)
    response = client.get("/proyectos/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_proyecto_sin_token():
    response = client.post("/proyectos/", json={"nombre": "P1", "descripcion": "D1"})
    assert response.status_code == 401