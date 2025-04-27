from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Usuario
from api.schemas.usuario import UsuarioSchema

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UsuarioSchema])
def obtener_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/{username}", response_model=UsuarioSchema)
def obtener_usuario(username: str, db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.username == username).first()

@router.post("/", response_model=UsuarioSchema)
def crear_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(
        username=usuario.username,
        contrasennia=usuario.contrasennia,
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        tipousuario_id=usuario.tipousuario_id
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.put("/{username}", response_model=UsuarioSchema)
def actualizar_usuario(username: str, usuario: UsuarioSchema, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.username == username).first()
    if usuario_db:
        usuario_db.contrasennia = usuario.contrasennia
        usuario_db.nombre = usuario.nombre
        usuario_db.apellido = usuario.apellido
        usuario_db.email = usuario.email
        usuario_db.tipousuario_id = usuario.tipousuario_id
        db.commit()
        db.refresh(usuario_db)
    return usuario_db

@router.delete("/{username}")
def eliminar_usuario(username: str, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.username == username).first()
    if usuario_db:
        db.delete(usuario_db)
        db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}