from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api.database import SessionLocal
from api.models import Direccion
from api.schemas.direccion import DireccionSchema, DireccionSchemaResponse

router = APIRouter(
    prefix="/direcciones",
    tags=["Direcciones"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[DireccionSchemaResponse])
def obtener_direcciones(db: Session = Depends(get_db)):
    return db.query(Direccion).all()

@router.get("/{iddireccion}", response_model=DireccionSchemaResponse)
def obtener_direccion(iddireccion: int, db: Session = Depends(get_db)):
    return db.query(Direccion).filter(Direccion.iddireccion == iddireccion).first()

@router.post("/", response_model=DireccionSchemaResponse)
def crear_direccion(direccion: DireccionSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_direccion_seq.NEXTVAL FROM dual")).scalar()

    nueva_direccion = Direccion(
        iddireccion=next_id,
        descripciondir=direccion.descripciondir,
        region_id=direccion.region_id,
        usuario_id=direccion.usuario_id
    )
    db.add(nueva_direccion)
    db.commit()
    db.refresh(nueva_direccion)
    return nueva_direccion

@router.put("/{iddireccion}", response_model=DireccionSchemaResponse)
def actualizar_direccion(iddireccion: int, direccion: DireccionSchema, db: Session = Depends(get_db)):
    direccion_db = db.query(Direccion).filter(Direccion.iddireccion == iddireccion).first()
    if direccion_db:
        direccion_db.descripciondir = direccion.descripciondir
        direccion_db.region_id = direccion.region_id
        direccion_db.usuario_id = direccion.usuario_id
        db.commit()
        db.refresh(direccion_db)
    return direccion_db

@router.delete("/{iddireccion}")
def eliminar_direccion(iddireccion: int, db: Session = Depends(get_db)):
    direccion_db = db.query(Direccion).filter(Direccion.iddireccion == iddireccion).first()
    if direccion_db:
        db.delete(direccion_db)
        db.commit()
    return {"mensaje": "Dirección eliminada correctamente"}