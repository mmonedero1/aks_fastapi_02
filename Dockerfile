# Usar Python 3.10 como imagen base
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar Poetry
RUN pip install --no-cache-dir poetry==1.7.1

# Configurar Poetry para no crear entornos virtuales
RUN poetry config virtualenvs.create false

# Copiar archivos de dependencias
COPY pyproject.toml poetry.lock* ./

# Instalar dependencias
RUN poetry install --no-interaction --no-ansi --no-root --only main

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
