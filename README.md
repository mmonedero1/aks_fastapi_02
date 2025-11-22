# API de Valoraciones con FastAPI

Servicio FastAPI con endpoint POST para gestionar valoraciones.

## Características

- Endpoint POST `/valoraciones` para crear valoraciones
- Dockerizado con Python 3.10 y Poetry
- Docker Compose para fácil despliegue

## Requisitos

- Docker
- Docker Compose

## Uso

### Construir y ejecutar con Docker Compose

```bash
docker-compose up --build
```

### Acceder a la API

- API: http://localhost:8000
- Documentación interactiva (Swagger): http://localhost:8000/docs
- Documentación alternativa (ReDoc): http://localhost:8000/redoc

### Ejemplo de petición POST

```bash
curl -X POST "http://localhost:8000/valoraciones" \
  -H "Content-Type: application/json" \
  -d '{
    "usuario": "Juan",
    "puntuacion": 5,
    "comentario": "Excelente producto",
    "producto_id": "prod-123"
  }'
```

## Desarrollo local con Poetry

```bash
# Instalar dependencias
poetry install

# Ejecutar la aplicación
poetry run uvicorn main:app --reload
```
