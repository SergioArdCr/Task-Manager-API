from sqlalchemy import Column, Integer, String, Enum
from app.db.database import Base
from pydantic import BaseModel
from typing import Optional
import enum

class RolEnum(str, enum.Enum):
    admin = "admin"
    member = "member"

class Usuario(Base):
    __tablename__ = "usuarios"
    id       = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    rol      = Column(String, default="member")

class UsuarioCreate(BaseModel):
    username: str
    password: str
    rol: Optional[str] = "member"

class Token(BaseModel):
    access_token: str
    token_type: str