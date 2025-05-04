from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    nombreproducto: str
    precioproducto: int
    especificacionprod: Optional[str] = None
    stockprod: int
    imagenprod: Optional[str] = None
    marca_id: int
    tipoprod_id: int
    idproducto: Optional[int]

    class Config:
        from_attributes = True
        
class ProductoUpdate(BaseModel):
    nombreproducto: Optional[str] = None
    precioproducto: Optional[float] = None
    especificacionprod: Optional[str] = None
    stockprod: Optional[int] = None
    imagenprod: Optional[str] = None
    marca_id: Optional[int] = None
    tipoprod_id: Optional[int] = None