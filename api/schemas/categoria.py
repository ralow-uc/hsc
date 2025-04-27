from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombrecat: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    idcategoria: int

    class Config:
        from_attributes = True