from pydantic import BaseModel

class RegionSchema(BaseModel):
    nombrereg: str
    comuna_id: int

    class Config:
        orm_mode = True

class RegionSchemaResponse(RegionSchema):
    idregion: int