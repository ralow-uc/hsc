from pydantic import BaseModel

class TipoUsuarioBase(BaseModel):
    nombretipo: str

class TipoUsuarioCreate(TipoUsuarioBase):
    pass

class TipoUsuarioUpdate(TipoUsuarioBase):
    pass

class TipoUsuarioSchema(TipoUsuarioBase):
    idtipousuario: int

    class Config:
        from_attributes = True