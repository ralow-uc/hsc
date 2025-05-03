from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api_auth.database import SessionLocal
from api_auth.models import TipoUsuario
from api_auth.schemas.tipousuario import TipoUsuarioSchema, TipoUsuarioCreate, TipoUsuarioUpdate

router = APIRouter(
    prefix="/tipousuarios",
    tags=["Tipo de Usuario"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[TipoUsuarioSchema])
def obtener_tipos_usuario(db: Session = Depends(get_db)):
    return db.query(TipoUsuario).all()

@router.get("/{idtipousuario}", response_model=TipoUsuarioSchema)
def obtener_tipo_usuario(idtipousuario: int, db: Session = Depends(get_db)):
    return db.query(TipoUsuario).filter(TipoUsuario.idtipousuario == idtipousuario).first()

@router.post("/", response_model=TipoUsuarioSchema)
def crear_tipo_usuario(tipo_usuario: TipoUsuarioCreate, db: Session = Depends(get_db)):
    nuevo_tipo_usuario = TipoUsuario(
        nombretipo=tipo_usuario.nombretipo
    )
    db.add(nuevo_tipo_usuario)
    db.commit()
    db.refresh(nuevo_tipo_usuario)
    return nuevo_tipo_usuario


@router.put("/{idtipousuario}", response_model=TipoUsuarioSchema)
def actualizar_tipo_usuario(idtipousuario: int, tipo_usuario: TipoUsuarioUpdate, db: Session = Depends(get_db)):
    tipo_usuario_db = db.query(TipoUsuario).filter(TipoUsuario.idtipousuario == idtipousuario).first()
    if tipo_usuario_db:
        tipo_usuario_db.nombretipo = tipo_usuario.nombretipo
        db.commit()
        db.refresh(tipo_usuario_db)
    return tipo_usuario_db

@router.delete("/{idtipousuario}")
def eliminar_tipo_usuario(idtipousuario: int, db: Session = Depends(get_db)):
    tipo_usuario_db = db.query(TipoUsuario).filter(TipoUsuario.idtipousuario == idtipousuario).first()
    if tipo_usuario_db:
        db.delete(tipo_usuario_db)
        db.commit()
    return {"mensaje": "Tipo de usuario eliminado correctamente"}