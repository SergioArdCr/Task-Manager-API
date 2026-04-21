from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config.settings import Ruta_DB

engine = create_engine(f"sqlite:///{Ruta_DB}")
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.models import usuario, proyecto, tarea
Base.metadata.create_all(bind=engine)