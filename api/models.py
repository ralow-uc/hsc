from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
from api.database import Base 

class Categoria(Base):
    __tablename__ = "INICIO_CATEGORIA"

    idcategoria = Column("IDCATEGORIA", Integer, primary_key=True, index=True)
    nombrecat = Column("NOMBRECAT", String(30))
    
class Producto(Base):
    __tablename__ = "INICIO_PRODUCTO"

    idproducto = Column(
        "IDPRODUCTO",
        Integer,
        Sequence('inicio_producto_seq'),
        primary_key=True,
        server_default=None
    )
    idproducto = Column("IDPRODUCTO", Integer, primary_key=True, index=True)
    nombreproducto = Column("NOMBREPRODUCTO", String(50))
    precioproducto = Column("PRECIOPRODUCTO", Integer)
    especificacionprod = Column("ESPECIFICACIONPROD", String(900))
    stockprod = Column("STOCKPROD", Integer)
    imagenprod = Column("IMAGENPROD", String(100))
    marca_id = Column("MARCA_ID", Integer, ForeignKey('INICIO_MARCA.IDMARCA'))
    tipoprod_id = Column("TIPOPROD_ID", Integer, ForeignKey('INICIO_TIPOPROD.IDTIPOROD'))

class Marca(Base):
    __tablename__ = "INICIO_MARCA"

    idmarca = Column("IDMARCA", Integer, primary_key=True, autoincrement=True)
    nombremarca = Column("NOMBREMARCA", String(30), nullable=False)

class Modelo(Base):
    __tablename__ = 'INICIO_MODELO'

    idmodelo = Column('IDMODELO', Integer, primary_key=True)
    nombremodelo = Column('NOMBREMODELO', String(30))
    marca_id = Column('MARCA_ID', Integer, ForeignKey('INICIO_MARCA.IDMARCA'))
    

class TipoProducto(Base):
    __tablename__ = "INICIO_TIPOPROD"

    idtipoprod = Column('IDTIPOROD', Integer, primary_key=True, index=True)
    nombretipoproducto = Column('NOMBRETIPOPROD', String(50))
