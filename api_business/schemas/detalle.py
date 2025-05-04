from pydantic import BaseModel

class DetalleSchema(BaseModel):
    cantidad: int
    subtotal: int
    producto_id: int
    venta_id: int

    class Config:
        orm_mode = True

class DetalleSchemaResponse(DetalleSchema):
    iddetalle: int