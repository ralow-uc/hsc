from pydantic import BaseModel
from typing import Optional

class DireccionSchema(BaseModel):
    descripciondir: str
    region_id: int
    usuario_id: str

    class Config:
        orm_mode = True

class DireccionSchemaResponse(DireccionSchema):
    iddireccion: int
    descripciondir: Optional[str]