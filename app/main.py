from fastapi import FastAPI
from app.src.routers import academico, auth
from app.src.middlewares import setup_middlewares

app = FastAPI(title="Api Gestión")

#Aplica middlewares
setup_middlewares(app)

# Incluir los routers
app.include_router(auth.router)
app.include_router(academico.router)

#ruta a la raíz---------------------------------------------------------------------------------------------------------------------------------------------------------------
@app.get("/")
async def root():
    return {"mensaje":"Este es un mensaje desde la Api"}
