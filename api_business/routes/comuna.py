from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api_business.database import SessionLocal
from api_business.models import Comuna
from api_business.schemas.comuna import ComunaSchema, ComunaSchemaResponse

router = APIRouter(
    prefix="/comunas",
    tags=["Comunas"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ComunaSchemaResponse])
def obtener_comunas(db: Session = Depends(get_db)):
    return db.query(Comuna).all()

@router.get("/{idcomuna}", response_model=ComunaSchemaResponse)
def obtener_comuna(idcomuna: int, db: Session = Depends(get_db)):
    return db.query(Comuna).filter(Comuna.idcomuna == idcomuna).first()

@router.post("/", response_model=ComunaSchemaResponse)
def crear_comuna(comuna: ComunaSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_comuna_seq.NEXTVAL FROM dual")).scalar()

    nueva_comuna = Comuna(
        idcomuna=next_id,
        nombrecom=comuna.nombrecom
    )
    db.add(nueva_comuna)
    db.commit()
    db.refresh(nueva_comuna)
    return nueva_comuna

@router.put("/{idcomuna}", response_model=ComunaSchemaResponse)
def actualizar_comuna(idcomuna: int, comuna: ComunaSchema, db: Session = Depends(get_db)):
    comuna_db = db.query(Comuna).filter(Comuna.idcomuna == idcomuna).first()
    if comuna_db:
        comuna_db.nombrecom = comuna.nombrecom
        db.commit()
        db.refresh(comuna_db)
    return comuna_db

@router.delete("/{idcomuna}")
def eliminar_comuna(idcomuna: int, db: Session = Depends(get_db)):
    comuna_db = db.query(Comuna).filter(Comuna.idcomuna == idcomuna).first()
    if comuna_db:
        db.delete(comuna_db)
        db.commit()
    return {"mensaje": "Comuna eliminada correctamente"}