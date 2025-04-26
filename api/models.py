from sqlalchemy import Column, Integer, String
from api.database import Base 

class Categoria(Base):
    __tablename__ = "INICIO_CATEGORIA"

    idcategoria = Column("IDCATEGORIA", Integer, primary_key=True, index=True)
    nombrecat = Column("NOMBRECAT", String(30))