from pydantic import BaseModel

class TipoProductoCreate(BaseModel):
    nombretipoproducto: str

class TipoProductoSchema(TipoProductoCreate):
    idtipoprod: int

    class Config:
        from_attributes = True