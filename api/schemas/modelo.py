from pydantic import BaseModel

class ModeloSchema(BaseModel):
    nombremodelo: str
    marca_id: int

    class Config:
        from_attributes = True