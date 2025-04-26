from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Categoria
from api.schemas.categoria import CategoriaCreate, Categoria as CategoriaSchema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/categorias", response_model=List[CategoriaSchema])
def listar_categorias(db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return categorias
  

@router.post("/categorias", response_model=CategoriaSchema)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    nueva_categoria = Categoria(
        nombrecat=categoria.nombrecat
    )
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria
  
@router.get("/categorias/{idcategoria}", response_model=CategoriaSchema)
def obtener_categoria(idcategoria: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.idcategoria == idcategoria).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@router.put("/categorias/{idcategoria}", response_model=CategoriaSchema)
def actualizar_categoria(idcategoria: int, categoria_actualizada: CategoriaCreate, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.idcategoria == idcategoria).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    categoria.nombrecat = categoria_actualizada.nombrecat
    db.commit()
    db.refresh(categoria)
    return categoria
  
@router.delete("/categorias/{idcategoria}")
def eliminar_categoria(idcategoria: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.idcategoria == idcategoria).first()
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    db.delete(categoria)
    db.commit()
    return {"mensaje": "Categoría eliminada correctamente"}
