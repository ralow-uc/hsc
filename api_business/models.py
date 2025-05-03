from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, Date, Text
from api_business.database import Base 

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

class Usuario(Base):
    __tablename__ = "INICIO_USUARIO"

    username = Column("USERNAME", String(15), primary_key=True)
    contrasennia = Column("CONTRASENNIA", String(30))
    nombre = Column("NOMBRE", String(60))
    apellido = Column("APELLIDO", String(60))
    email = Column("EMAIL", String(150))
    tipousuario_id = Column("TIPOUSUARIO_ID", Integer, ForeignKey('INICIO_TIPOUSUARIO.IDTIPOUSUARIO'))
    
    
class TipoUsuario(Base):
    __tablename__ = "INICIO_TIPOUSUARIO"

    idtipousuario = Column("IDTIPOUSUARIO", Integer, primary_key=True, index=True)
    nombretipo = Column("NOMBRETIPO", String(30))
    
class Comuna(Base):
    __tablename__ = "INICIO_COMUNA"

    idcomuna = Column("IDCOMUNA", Integer, primary_key=True, index=True)
    nombrecom = Column("NOMBRECOM", String(40))
    
class Region(Base):
    __tablename__ = "INICIO_REGION"

    idregion = Column("IDREGION", Integer, primary_key=True, index=True)
    nombrereg = Column("NOMBREREG", String(40))
    comuna_id = Column("COMUNA_ID", Integer, ForeignKey('INICIO_COMUNA.IDCOMUNA'))

class Direccion(Base):
    __tablename__ = "INICIO_DIRECCION"

    iddireccion = Column("IDDIRECCION", Integer, primary_key=True, index=True)
    descripciondir = Column("DESCRIPCIONDIR", Text)
    region_id = Column("REGION_ID", Integer, ForeignKey('INICIO_REGION.IDREGION'))
    usuario_id = Column("USUARIO_ID", String(15), ForeignKey('INICIO_USUARIO.USERNAME'))
    

class Venta(Base):
    __tablename__ = "INICIO_VENTA"

    idventa = Column("IDVENTA", Integer, primary_key=True, index=True)
    fechaventa = Column("FECHAVENTA", Date)
    usuario_id = Column("USUARIO_ID", String(15), ForeignKey('INICIO_USUARIO.USERNAME'))
    
class Detalle(Base):
    __tablename__ = "INICIO_DETALLE"

    iddetalle = Column("IDDETALLE", Integer, primary_key=True, index=True)
    cantidad = Column("CANTIDAD", Integer)
    subtotal = Column("SUBTOTAL", Integer)
    producto_id = Column("PRODUCTO_ID", Integer, ForeignKey('INICIO_PRODUCTO.IDPRODUCTO'))
    venta_id = Column("VENTA_ID", Integer, ForeignKey('INICIO_VENTA.IDVENTA'))