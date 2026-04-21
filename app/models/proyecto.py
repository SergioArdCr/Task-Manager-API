from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.database import Base
from pydantic import BaseModel

# tabla intermedia para la relación muchos a muchos
proyecto_miembros = Table(
    "proyecto_miembros",
    Base.metadata,
    Column("proyecto_id", Integer, ForeignKey("proyectos.id")),
    Column("usuario_id", Integer, ForeignKey("usuarios.id"))
)

class Proyecto(Base):
    __tablename__ = "proyectos"
    id          = Column(Integer, primary_key=True, autoincrement=True)
    nombre      = Column(String)
    descripcion = Column(String)
    owner_id    = Column(Integer, ForeignKey("usuarios.id"))
    miembros    = relationship("Usuario", secondary=proyecto_miembros)

class ProyectoCreate(BaseModel):
    nombre: str
    descripcion: str