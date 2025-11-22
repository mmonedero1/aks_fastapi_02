from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Servicio de Valoraciones")


class Valoracion(BaseModel):
    """Modelo para las valoraciones"""
    usuario: str
    puntuacion: int
    comentario: Optional[str] = None
    producto_id: Optional[str] = None


@app.get("/")
async def root():
    """Endpoint raíz"""
    return {"message": "Servicio de Valoraciones API"}


@app.post("/valoraciones")
async def crear_valoracion(valoracion: Valoracion):
    """
    Endpoint POST para crear valoraciones
    
    Args:
        valoracion: Datos de la valoración
        
    Returns:
        Confirmación de la valoración creada
    """
    return {
        "status": "success",
        "message": "Valoración creada correctamente",
        "data": valoracion.dict()
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
