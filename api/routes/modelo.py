from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Modelo
from api.schemas.modelo import ModeloSchema
from sqlalchemy import text

router = APIRouter(
    prefix="/modelos",
    tags=["Modelos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ModeloSchema], tags=["Modelos"])
def listar_modelos(db: Session = Depends(get_db)):
    return db.query(Modelo).all()

@router.get("/{idmodelo}", response_model=ModeloSchema, tags=["Modelos"])
def obtener_modelo(idmodelo: int, db: Session = Depends(get_db)):
    return db.query(Modelo).filter(Modelo.idmodelo == idmodelo).first()

@router.post("/", response_model=ModeloSchema, tags=["Modelos"])
def crear_modelo(modelo: ModeloSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_modelo_seq.NEXTVAL FROM dual")).scalar()

    nuevo_modelo = Modelo(
        idmodelo=next_id,
        nombremodelo=modelo.nombremodelo,
        marca_id=modelo.marca_id
    )
    db.add(nuevo_modelo)
    db.commit()
    db.refresh(nuevo_modelo)
    return nuevo_modelo

@router.put("/{idmodelo}", response_model=ModeloSchema, tags=["Modelos"])
def actualizar_modelo(idmodelo: int, modelo_actualizado: ModeloSchema, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).filter(Modelo.idmodelo == idmodelo).first()
    if modelo:
        modelo.nombremodelo = modelo_actualizado.nombremodelo
        modelo.marca_id = modelo_actualizado.marca_id
        db.commit()
        db.refresh(modelo)
    return modelo

@router.delete("/{idmodelo}", tags=["Modelos"])
def eliminar_modelo(idmodelo: int, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).filter(Modelo.idmodelo == idmodelo).first()
    if modelo:
        db.delete(modelo)
        db.commit()
    return {"message": "Modelo eliminado correctamente"}