# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

def setup(client):
    client.post("/auth/register", json={"username": "tarea_user", "password": "1234"})
    response = client.post("/auth/login", data={"username": "tarea_user", "password": "1234"})
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    proyecto = client.post("/proyectos/", json={"nombre": "P", "descripcion": "D"}, headers=headers)
    return token, headers, proyecto.json()["id"]

def test_crear_tarea(client):
    token, headers, proyecto_id = setup(client)
    response = client.post(f"/proyectos/{proyecto_id}/tareas", json={
        "titulo": "Tarea test",
        "descripcion": "Descripción",
        "prioridad": "high"
    }, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_tareas(client):
    token, headers, proyecto_id = setup(client)
    client.post(f"/proyectos/{proyecto_id}/tareas", json={
        "titulo": "T1", "descripcion": "D1"
    }, headers=headers)
    response = client.get(f"/proyectos/{proyecto_id}/tareas", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filtro_estado(client):
    token, headers, proyecto_id = setup(client)
    client.post(f"/proyectos/{proyecto_id}/tareas", json={
        "titulo": "T1", "descripcion": "D1"
    }, headers=headers)
    response = client.get(f"/proyectos/{proyecto_id}/tareas?estado=pending", headers=headers)
    assert response.status_code == 200

def test_actualizar_tarea(client):
    token, headers, proyecto_id = setup(client)
    tarea = client.post(f"/proyectos/{proyecto_id}/tareas", json={
        "titulo": "T1", "descripcion": "D1"
    }, headers=headers)
    tarea_id = tarea.json()["id"]
    response = client.put(f"/proyectos/{proyecto_id}/tareas/{tarea_id}", json={
        "estado": "done"
    }, headers=headers)
    assert response.status_code == 200

def test_eliminar_tarea(client):
    token, headers, proyecto_id = setup(client)
    tarea = client.post(f"/proyectos/{proyecto_id}/tareas", json={
        "titulo": "T1", "descripcion": "D1"
    }, headers=headers)
    tarea_id = tarea.json()["id"]
    response = client.delete(f"/proyectos/{proyecto_id}/tareas/{tarea_id}", headers=headers)
    assert response.status_code == 200