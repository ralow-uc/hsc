from pydantic import BaseModel

class Marca(BaseModel):
    nombremarca: str

    class Config:
        from_attributes = True
