from fastapi import FastAPI
from app.routers import auth, proyectos, tareas

app = FastAPI(title="Task Manager API")

app.include_router(auth.router)
app.include_router(proyectos.router)
app.include_router(tareas.router)