from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_business.routes import categoria, producto, marca, modelo, tipoproducto, comuna, region, direccion, venta, detalle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categoria.router)
app.include_router(producto.router)
app.include_router(marca.router)
app.include_router(modelo.router)
app.include_router(tipoproducto.router)
app.include_router(comuna.router)
app.include_router(region.router)
app.include_router(direccion.router)
app.include_router(venta.router)
app.include_router(detalle.router)