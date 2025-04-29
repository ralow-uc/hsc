from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api.database import SessionLocal
from api.models import Detalle
from api.schemas.detalle import DetalleSchema, DetalleSchemaResponse

router = APIRouter(
    prefix="/detalles",
    tags=["Detalles de Venta"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[DetalleSchemaResponse])
def obtener_detalles(db: Session = Depends(get_db)):
    return db.query(Detalle).all()

@router.get("/{iddetalle}", response_model=DetalleSchemaResponse)
def obtener_detalle(iddetalle: int, db: Session = Depends(get_db)):
    return db.query(Detalle).filter(Detalle.iddetalle == iddetalle).first()

@router.post("/", response_model=DetalleSchemaResponse)
def crear_detalle(detalle: DetalleSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_detalle_seq.NEXTVAL FROM dual")).scalar()

    nuevo_detalle = Detalle(
        iddetalle=next_id,
        cantidad=detalle.cantidad,
        subtotal=detalle.subtotal,
        producto_id=detalle.producto_id,
        venta_id=detalle.venta_id
    )
    db.add(nuevo_detalle)
    db.commit()
    db.refresh(nuevo_detalle)
    return nuevo_detalle

@router.put("/{iddetalle}", response_model=DetalleSchemaResponse)
def actualizar_detalle(iddetalle: int, detalle: DetalleSchema, db: Session = Depends(get_db)):
    detalle_db = db.query(Detalle).filter(Detalle.iddetalle == iddetalle).first()
    if detalle_db:
        detalle_db.cantidad = detalle.cantidad
        detalle_db.subtotal = detalle.subtotal
        detalle_db.producto_id = detalle.producto_id
        detalle_db.venta_id = detalle.venta_id
        db.commit()
        db.refresh(detalle_db)
    return detalle_db

@router.delete("/{iddetalle}")
def eliminar_detalle(iddetalle: int, db: Session = Depends(get_db)):
    detalle_db = db.query(Detalle).filter(Detalle.iddetalle == iddetalle).first()
    if detalle_db:
        db.delete(detalle_db)
        db.commit()
    return {"mensaje": "Detalle eliminado correctamente"}