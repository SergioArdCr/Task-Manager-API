from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.db.database import get_db
from app.models.tarea import Tarea, TareaCreate, TareaUpdate
from app.models.proyecto import Proyecto
from app.models.usuario import Usuario
from app.services.auth_services import get_current_user

router = APIRouter(prefix="/proyectos", tags=["Tareas"])

@router.post("/{proyecto_id}/tareas")
def crear_tarea(proyecto_id: int, body: TareaCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    nueva = Tarea(
        titulo=body.titulo,
        descripcion=body.descripcion,
        prioridad=body.prioridad,
        asignado_a=body.asignado_a,
        proyecto_id=proyecto_id
    )
    db.add(nueva)
    db.commit()
    return {"message": "Tarea creada", "id": nueva.id}

@router.get("/{proyecto_id}/tareas")
def get_tareas(
    proyecto_id: int,
    estado: Optional[str] = None,
    prioridad: Optional[str] = None,
    asignado_a: Optional[int] = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(Tarea).filter(Tarea.proyecto_id == proyecto_id)
    if estado:
        query = query.filter(Tarea.estado == estado)
    if prioridad:
        query = query.filter(Tarea.prioridad == prioridad)
    if asignado_a:
        query = query.filter(Tarea.asignado_a == asignado_a)
    return query.all()

@router.put("/{proyecto_id}/tareas/{tarea_id}")
def actualizar_tarea(proyecto_id: int, tarea_id: int, body: TareaUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.proyecto_id == proyecto_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if body.estado:
        tarea.estado = body.estado
    if body.prioridad:
        tarea.prioridad = body.prioridad
    if body.asignado_a:
        tarea.asignado_a = body.asignado_a
    db.commit()
    return {"message": f"Tarea {tarea_id} actualizada"}

@router.delete("/{proyecto_id}/tareas/{tarea_id}")
def eliminar_tarea(proyecto_id: int, tarea_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id, Tarea.proyecto_id == proyecto_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(tarea)
    db.commit()
    return {"message": f"Tarea {tarea_id} eliminada"}