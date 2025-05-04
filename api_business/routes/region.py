from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from api_business.database import SessionLocal
from api_business.models import Region
from api_business.schemas.region import RegionSchema, RegionSchemaResponse

router = APIRouter(
    prefix="/regiones",
    tags=["Regiones"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[RegionSchemaResponse])
def obtener_regiones(db: Session = Depends(get_db)):
    return db.query(Region).all()

@router.get("/{idregion}", response_model=RegionSchemaResponse)
def obtener_region(idregion: int, db: Session = Depends(get_db)):
    return db.query(Region).filter(Region.idregion == idregion).first()

@router.post("/", response_model=RegionSchemaResponse)
def crear_region(region: RegionSchema, db: Session = Depends(get_db)):
    next_id = db.execute(text("SELECT inicio_region_seq.NEXTVAL FROM dual")).scalar()

    nueva_region = Region(
        idregion=next_id,
        nombrereg=region.nombrereg,
        comuna_id=region.comuna_id
    )
    db.add(nueva_region)
    db.commit()
    db.refresh(nueva_region)
    return nueva_region

@router.put("/{idregion}", response_model=RegionSchemaResponse)
def actualizar_region(idregion: int, region: RegionSchema, db: Session = Depends(get_db)):
    region_db = db.query(Region).filter(Region.idregion == idregion).first()
    if region_db:
        region_db.nombrereg = region.nombrereg
        region_db.comuna_id = region.comuna_id
        db.commit()
        db.refresh(region_db)
    return region_db

@router.delete("/{idregion}")
def eliminar_region(idregion: int, db: Session = Depends(get_db)):
    region_db = db.query(Region).filter(Region.idregion == idregion).first()
    if region_db:
        db.delete(region_db)
        db.commit()
    return {"mensaje": "Región eliminada correctamente"}