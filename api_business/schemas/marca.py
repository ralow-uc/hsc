from pydantic import BaseModel

class Marca(BaseModel):
    idmarca: int
    nombremarca: str

    class Config:
        from_attributes = True
