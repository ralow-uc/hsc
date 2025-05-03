from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    username: str
    contrasennia: str
    nombre: str
    apellido: str
    email: str
    tipousuario_id: int

    class Config:
        from_attributes = True
