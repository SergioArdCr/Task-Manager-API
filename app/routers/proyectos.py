from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.proyecto import Proyecto, ProyectoCreate
from app.models.usuario import Usuario
from app.services.auth_services import get_current_user

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])

@router.post("/")
def crear_proyecto(body: ProyectoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    owner = db.query(Usuario).filter(Usuario.username == user["sub"]).first()
    nuevo = Proyecto(nombre=body.nombre, descripcion=body.descripcion, owner_id=owner.id)
    nuevo.miembros.append(owner)  # el creador es miembro automáticamente
    db.add(nuevo)
    db.commit()
    return {"message": "Proyecto creado", "id": nuevo.id}

@router.get("/")
def get_proyectos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    owner = db.query(Usuario).filter(Usuario.username == user["sub"]).first()
    return db.query(Proyecto).filter(Proyecto.owner_id == owner.id).all()

@router.post("/{proyecto_id}/miembros/{usuario_id}")
def agregar_miembro(proyecto_id: int, usuario_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    owner = db.query(Usuario).filter(Usuario.username == user["sub"]).first()
    if proyecto.owner_id != owner.id:
        raise HTTPException(status_code=403, detail="Solo el owner puede agregar miembros")
    nuevo_miembro = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not nuevo_miembro:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    proyecto.miembros.append(nuevo_miembro)
    db.commit()
    return {"message": f"Usuario {nuevo_miembro.username} agregado al proyecto"}