from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api.database import SessionLocal
from api.models import Venta
from api.schemas.venta import VentaSchema, VentaSchemaResponse

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[VentaSchemaResponse])
def obtener_ventas(db: Session = Depends(get_db)):
    return db.query(Venta).all()

@router.get("/{idventa}", response_model=VentaSchemaResponse)
def obtener_venta(idventa: int, db: Session = Depends(get_db)):
    return db.query(Venta).filter(Venta.idventa == idventa).first()

@router.post("/", response_model=VentaSchemaResponse)
def crear_venta(venta: VentaSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_venta_seq.NEXTVAL FROM dual")).scalar()

    nueva_venta = Venta(
        idventa=next_id,
        fechaventa=venta.fechaventa,
        usuario_id=venta.usuario_id
    )
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

@router.put("/{idventa}", response_model=VentaSchemaResponse)
def actualizar_venta(idventa: int, venta: VentaSchema, db: Session = Depends(get_db)):
    venta_db = db.query(Venta).filter(Venta.idventa == idventa).first()
    if venta_db:
        venta_db.fechaventa = venta.fechaventa
        venta_db.usuario_id = venta.usuario_id
        db.commit()
        db.refresh(venta_db)
    return venta_db

@router.delete("/{idventa}")
def eliminar_venta(idventa: int, db: Session = Depends(get_db)):
    venta_db = db.query(Venta).filter(Venta.idventa == idventa).first()
    if venta_db:
        db.delete(venta_db)
        db.commit()
    return {"mensaje": "Venta eliminada correctamente"}