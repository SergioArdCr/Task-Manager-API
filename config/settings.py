import os
from dotenv import load_dotenv

Ruta_Base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas y archivos

Ruta_DB = os.path.join(Ruta_Base, "data", "Task_Manager.db")

# .env 

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")   # clave para firmar el JWT
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30
