from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from config.settings import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hashear(password: str) -> str:
    return pwd_context.hash(password)

def verificar(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def crear_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
    
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return payload