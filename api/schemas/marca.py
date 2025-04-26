from pydantic import BaseModel

class Marca(BaseModel):
    nombremarca: str

    class Config:
        orm_mode = True
