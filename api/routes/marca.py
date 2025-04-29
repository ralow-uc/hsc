from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List
from api.database import SessionLocal
from api.models import Marca as MarcaModel
from api.schemas.marca import Marca as MarcaSchema

router = APIRouter(
    prefix="/marcas",
    tags=["Marcas"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[MarcaSchema])
def listar_marcas(db: Session = Depends(get_db)):
    return db.query(MarcaModel).all()

@router.post("/", response_model=MarcaSchema, tags=["Marcas"])
def crear_marca(marca: MarcaSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_marca_seq.NEXTVAL FROM dual")).scalar()
    
    nueva_marca = MarcaModel(
        idmarca=next_id,
        nombremarca=marca.nombremarca
    )
    db.add(nueva_marca)
    db.commit()
    db.refresh(nueva_marca)
    return nueva_marca

@router.put("/{idmarca}", response_model=MarcaSchema)
def actualizar_marca(idmarca: int, marca_actualizada: MarcaSchema, db: Session = Depends(get_db)):
    marca = db.query(MarcaModel).filter(MarcaModel.idmarca == idmarca).first()
    if marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")

    marca.nombremarca = marca_actualizada.nombremarca
    db.commit()
    db.refresh(marca)
    return marca

@router.delete("/{idmarca}")
def eliminar_marca(idmarca: int, db: Session = Depends(get_db)):
    marca = db.query(MarcaModel).filter(MarcaModel.idmarca == idmarca).first()
    if marca is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")

    db.delete(marca)
    db.commit()
    return {"detail": "Marca eliminada correctamente"}
