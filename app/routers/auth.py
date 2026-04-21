from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.usuario import Usuario, UsuarioCreate, Token
from app.services.auth_services import hashear, verificar, crear_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(body: UsuarioCreate, db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter(Usuario.username == body.username).first()
    if existe:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    nuevo = Usuario(username=body.username, password=hashear(body.password), rol=body.rol)
    db.add(nuevo)
    db.commit()
    return {"message": "Usuario creado", "rol": body.rol}

@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.username == form.username).first()
    if not usuario or not verificar(form.password, usuario.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = crear_token({"sub": usuario.username, "rol": usuario.rol})
    return {"access_token": token, "token_type": "bearer"}