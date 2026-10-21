from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.src.config import CORS_ORIGIN

def setup_middlewares(app: FastAPI) -> None:
    """
    Configura y registra todos los middlewares de la aplicación.
    """
    
    # 1. Configuración de CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins= CORS_ORIGIN,
        allow_credentials= True,
        allow_methods= ["*"],
        allow_headers=["*",]
    )