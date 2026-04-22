# ✅ Task Manager API (Español)

---

## 📌 Descripción

API REST para gestión de proyectos y tareas construida con FastAPI y SQLAlchemy. Permite crear proyectos, invitar miembros, crear tareas con estados y prioridades, asignarlas a usuarios y filtrarlas. Incluye autenticación JWT con roles, Docker y deploy en Railway.

Proyecto final desarrollado como parte de un plan de aprendizaje de Python enfocado en desarrollo backend.

**URL en producción:** https://task-manager-api-production-36bd.up.railway.app/docs

## 🛠️ Tecnologías

- `FastAPI` — framework web para construir la API
- `SQLAlchemy` — ORM para manejo de base de datos
- `SQLite` — base de datos relacional
- `JWT` + `bcrypt` — autenticación con roles y hashing de contraseñas
- `pytest` — tests automatizados
- `Docker` — contenedorización
- `Railway` — deploy en producción

## 📁 Estructura

```
app/
├── main.py
├── db/
│   └── database.py
├── models/
│   ├── usuario.py
│   ├── proyecto.py
│   └── tarea.py
├── routers/
│   ├── auth.py
│   ├── proyectos.py
│   └── tareas.py
└── services/
    └── auth_service.py
config/
└── settings.py
data/
tests/
├── test_auth.py
├── test_proyectos.py
└── test_tareas.py
Dockerfile
requirements.txt
```

## 🗃️ Relaciones entre tablas

```
usuarios
    ↓ crea
proyectos ←→ usuarios (muchos a muchos: proyecto_miembros)
    ↓ contiene
tareas → asignada a → usuarios
```

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/Task-Manager-API.git
cd Task-Manager-API

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
echo "SECRET_KEY=tu_clave_secreta" > .env

# Correr el servidor
uvicorn app.main:app --reload
```

## 🐳 Correr con Docker

```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
```

## 🔐 Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```
SECRET_KEY=tu_clave_secreta
```

## 🚀 Endpoints

### Autenticación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/register` | Registrar nuevo usuario (`admin` o `member`) |
| POST | `/auth/login` | Login y obtener token JWT |

### Proyectos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/proyectos/` | Crear proyecto |
| GET | `/proyectos/` | Obtener proyectos del usuario |
| POST | `/proyectos/{id}/miembros/{user_id}` | Agregar miembro al proyecto |

### Tareas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/proyectos/{id}/tareas` | Crear tarea |
| GET | `/proyectos/{id}/tareas` | Obtener tareas (con filtros) |
| PUT | `/proyectos/{id}/tareas/{tarea_id}` | Actualizar tarea |
| DELETE | `/proyectos/{id}/tareas/{tarea_id}` | Eliminar tarea |

### Filtros disponibles

```
GET /proyectos/{id}/tareas?estado=pending
GET /proyectos/{id}/tareas?prioridad=high
GET /proyectos/{id}/tareas?asignado_a=1
GET /proyectos/{id}/tareas?estado=in_progress&prioridad=high
```

## 🧪 Correr tests

```bash
pytest tests/ -v
```

## 💡 Ejemplo de uso

```python
import httpx

BASE_URL = "https://task-manager-api-production-36bd.up.railway.app"

# Registro y login
httpx.post(f"{BASE_URL}/auth/register", json={"username": "sergio", "password": "1234", "rol": "admin"})
response = httpx.post(f"{BASE_URL}/auth/login", data={"username": "sergio", "password": "1234"})
token = response.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Crear proyecto
proyecto = httpx.post(f"{BASE_URL}/proyectos/", json={"nombre": "Mi Proyecto", "descripcion": "Descripción"}, headers=headers)
proyecto_id = proyecto.json()["id"]

# Crear tarea
httpx.post(f"{BASE_URL}/proyectos/{proyecto_id}/tareas", json={
    "titulo": "Primera tarea",
    "descripcion": "Descripción de la tarea",
    "prioridad": "high"
}, headers=headers)

# Filtrar tareas por prioridad
tareas = httpx.get(f"{BASE_URL}/proyectos/{proyecto_id}/tareas?prioridad=high", headers=headers)
print(tareas.json())
```

## 💡 Aprendizajes clave

- Relaciones muchos a muchos con tabla intermedia en SQLAlchemy
- Autenticación JWT con roles (`admin` / `member`)
- Filtros dinámicos con parámetros opcionales en FastAPI
- Lógica de permisos — solo el owner puede agregar miembros
- Testing completo de auth, proyectos y tareas con pytest
- Contenedorización con Docker y deploy en Railway

---

---

# ✅ Task Manager API (English)

---

## 📌 Description

REST API for project and task management built with FastAPI and SQLAlchemy. Allows creating projects, inviting members, creating tasks with states and priorities, assigning them to users, and filtering them. Includes JWT authentication with roles, Docker and Railway deployment.

Built as the final project of a Python learning plan focused on backend development.

**Live URL:** https://task-manager-api-production-36bd.up.railway.app/docs

## 🛠️ Tech Stack

- `FastAPI` — web framework for building the API
- `SQLAlchemy` — ORM for database management
- `SQLite` — relational database
- `JWT` + `bcrypt` — role-based authentication and password hashing
- `pytest` — automated tests
- `Docker` — containerization
- `Railway` — production deploy

## 📁 Structure

```
app/
├── main.py
├── db/
│   └── database.py
├── models/
│   ├── usuario.py
│   ├── proyecto.py
│   └── tarea.py
├── routers/
│   ├── auth.py
│   ├── proyectos.py
│   └── tareas.py
└── services/
    └── auth_service.py
config/
└── settings.py
data/
tests/
├── test_auth.py
├── test_proyectos.py
└── test_tareas.py
Dockerfile
requirements.txt
```

## 🗃️ Database Relations

```
usuarios
    ↓ creates
proyectos ←→ usuarios (many-to-many: proyecto_miembros)
    ↓ contains
tareas → assigned to → usuarios
```

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/Task-Manager-API.git
cd Task-Manager-API

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "SECRET_KEY=your_secret_key" > .env

# Run the server
uvicorn app.main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
```

## 🔐 Environment Variables

Create a `.env` file at the project root:

```
SECRET_KEY=your_secret_key
```

## 🚀 Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user (`admin` or `member`) |
| POST | `/auth/login` | Login and get JWT token |

### Projects
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/proyectos/` | Create project |
| GET | `/proyectos/` | Get user's projects |
| POST | `/proyectos/{id}/miembros/{user_id}` | Add member to project |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/proyectos/{id}/tareas` | Create task |
| GET | `/proyectos/{id}/tareas` | Get tasks (supports filters) |
| PUT | `/proyectos/{id}/tareas/{tarea_id}` | Update task |
| DELETE | `/proyectos/{id}/tareas/{tarea_id}` | Delete task |

### Available Filters

```
GET /proyectos/{id}/tareas?estado=pending
GET /proyectos/{id}/tareas?prioridad=high
GET /proyectos/{id}/tareas?asignado_a=1
GET /proyectos/{id}/tareas?estado=in_progress&prioridad=high
```

## 🧪 Run Tests

```bash
pytest tests/ -v
```

## 💡 Usage Example

```python
import httpx

BASE_URL = "https://task-manager-api-production-36bd.up.railway.app"

# Register and login
httpx.post(f"{BASE_URL}/auth/register", json={"username": "sergio", "password": "1234", "rol": "admin"})
response = httpx.post(f"{BASE_URL}/auth/login", data={"username": "sergio", "password": "1234"})
token = response.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Create project
project = httpx.post(f"{BASE_URL}/proyectos/", json={"nombre": "My Project", "descripcion": "Description"}, headers=headers)
project_id = project.json()["id"]

# Create task
httpx.post(f"{BASE_URL}/proyectos/{project_id}/tareas", json={
    "titulo": "First task",
    "descripcion": "Task description",
    "prioridad": "high"
}, headers=headers)

# Filter tasks by priority
tasks = httpx.get(f"{BASE_URL}/proyectos/{project_id}/tareas?prioridad=high", headers=headers)
print(tasks.json())
```

## 💡 Key Learnings

- Many-to-many relationships with intermediate table in SQLAlchemy
- JWT authentication with roles (`admin` / `member`)
- Dynamic filters with optional query parameters in FastAPI
- Permission logic — only the owner can add members
- Full test coverage for auth, projects and tasks with pytest
- Docker containerization and Railway deployment
