from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base
from pydantic import BaseModel
from typing import Optional

class Tarea(Base):
    __tablename__ = "tareas"
    id           = Column(Integer, primary_key=True, autoincrement=True)
    titulo       = Column(String)
    descripcion  = Column(String)
    estado       = Column(String, default="pending")    # pending, in_progress, done
    prioridad    = Column(String, default="medium")     # low, medium, high
    proyecto_id  = Column(Integer, ForeignKey("proyectos.id"))
    asignado_a   = Column(Integer, ForeignKey("usuarios.id"), nullable=True)

class TareaCreate(BaseModel):
    titulo: str
    descripcion: str
    prioridad: Optional[str] = "medium"
    asignado_a: Optional[int] = None

class TareaUpdate(BaseModel):
    estado: Optional[str] = None
    prioridad: Optional[str] = None
    asignado_a: Optional[int] = None