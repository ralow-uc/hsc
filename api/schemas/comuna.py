from pydantic import BaseModel

class ComunaSchema(BaseModel):
    nombrecom: str

    class Config:
        orm_mode = True

class ComunaSchemaResponse(ComunaSchema):
    idcomuna: int