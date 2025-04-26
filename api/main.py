from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import categoria, producto, marca

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