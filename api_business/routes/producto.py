from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from api_business.database import SessionLocal
from api_business.models import Producto as ProductoModel
from api_business.schemas.producto import Producto as ProductoSchema, ProductoCreate, ProductoUpdate

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProductoSchema], tags=["Productos"])
def listar_productos(db: Session = Depends(get_db)):
    productos = db.query(ProductoModel).all()
    return productos

@router.get("/{idproducto}", response_model=ProductoSchema, tags=["Productos"])
def obtener_producto(idproducto: int, db: Session = Depends(get_db)):
    producto = db.query(ProductoModel).filter(ProductoModel.idproducto == idproducto).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoSchema, tags=["Productos"])
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_producto_seq.NEXTVAL FROM dual")).scalar()
  
    nuevo_producto = ProductoModel(
        idproducto=next_id,
        nombreproducto=producto.nombreproducto,
        precioproducto=producto.precioproducto,
        especificacionprod=producto.especificacionprod,
        stockprod=producto.stockprod,
        imagenprod=producto.imagenprod,
        marca_id=producto.marca_id,
        tipoprod_id=producto.tipoprod_id
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@router.put("/{idproducto}", response_model=ProductoSchema, tags=["Productos"])
def actualizar_producto(idproducto: int, producto_actualizado: ProductoUpdate, db: Session = Depends(get_db)):
    producto = db.query(ProductoModel).filter(ProductoModel.idproducto == idproducto).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto_actualizado.nombreproducto is not None:
        producto.nombreproducto = producto_actualizado.nombreproducto
    if producto_actualizado.precioproducto is not None:
        producto.precioproducto = producto_actualizado.precioproducto
    if producto_actualizado.especificacionprod is not None:
        producto.especificacionprod = producto_actualizado.especificacionprod
    if producto_actualizado.stockprod is not None:
        producto.stockprod = producto_actualizado.stockprod
    if producto_actualizado.imagenprod is not None:
        producto.imagenprod = producto_actualizado.imagenprod
    if producto_actualizado.marca_id is not None:
        producto.marca_id = producto_actualizado.marca_id
    if producto_actualizado.tipoprod_id is not None:
        producto.tipoprod_id = producto_actualizado.tipoprod_id

    db.commit()
    db.refresh(producto)
    return producto

@router.delete("/{idproducto}", tags=["Productos"])
def eliminar_producto(idproducto: int, db: Session = Depends(get_db)):
    producto = db.query(ProductoModel).filter(ProductoModel.idproducto == idproducto).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()
    return {"message": "Producto eliminado correctamente"}

@router.get("/tipo/{tipoprod_id}", response_model=List[ProductoSchema], tags=["Productos"])
def obtener_productos_por_tipo(tipoprod_id: int, db: Session = Depends(get_db)):
    productos = db.query(ProductoModel).filter(ProductoModel.tipoprod_id == tipoprod_id).all()
    return productos