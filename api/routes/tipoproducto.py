from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api.database import SessionLocal
from api.models import TipoProducto
from api.schemas.tipoproducto import TipoProductoSchema, TipoProductoCreate

router = APIRouter(
    prefix="/tipoproducto",
    tags=["Tipo de Producto"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[TipoProductoSchema])
def obtener_tipos_producto(db: Session = Depends(get_db)):
    return db.query(TipoProducto).all()

@router.get("/{idtipoprod}", response_model=TipoProductoSchema)
def obtener_tipo_producto(idtipoprod: int, db: Session = Depends(get_db)):
    return db.query(TipoProducto).filter(TipoProducto.idtipoprod == idtipoprod).first()

@router.post("/", response_model=TipoProductoSchema)
def crear_tipo_producto(tipo_producto: TipoProductoCreate, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_tipoproducto_seq.NEXTVAL FROM dual")).scalar()

    nuevo_tipo_producto = TipoProducto(
        idtipoprod=next_id,
        nombretipoproducto=tipo_producto.nombretipoproducto
    )
    db.add(nuevo_tipo_producto)
    db.commit()
    db.refresh(nuevo_tipo_producto)
    return nuevo_tipo_producto

@router.put("/{idtipoprod}", response_model=TipoProductoSchema)
def actualizar_tipo_producto(idtipoprod: int, tipo_producto: TipoProductoCreate, db: Session = Depends(get_db)):
    tipo_prod_db = db.query(TipoProducto).filter(TipoProducto.idtipoprod == idtipoprod).first()
    if tipo_prod_db:
        tipo_prod_db.nombretipoproducto = tipo_producto.nombretipoproducto
        db.commit()
        db.refresh(tipo_prod_db)
    return tipo_prod_db

@router.delete("/{idtipoprod}")
def eliminar_tipo_producto(idtipoprod: int, db: Session = Depends(get_db)):
    tipo_prod_db = db.query(TipoProducto).filter(TipoProducto.idtipoprod == idtipoprod).first()
    if tipo_prod_db:
        db.delete(tipo_prod_db)
        db.commit()
    return {"mensaje": "Tipo de producto eliminado correctamente"}