from pydantic import BaseModel
from datetime import date

class VentaSchema(BaseModel):
    fechaventa: date
    usuario_id: str

    class Config:
        orm_mode = True

class VentaSchemaResponse(VentaSchema):
    idventa: int