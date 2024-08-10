# Usamos una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /EDA

# Copiar los archivos de Poetry y pyproject.toml al contenedor
COPY pyproject.toml poetry.lock* /EDA/

# Instalar Poetry
RUN pip install poetry

# Instalar las dependencias del proyecto sin crear un entorno virtual dentro del contenedor
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copiar el resto del código de la aplicación al contenedor
COPY . /EDA/

# Comando para ejecutar la aplicación, este será reemplazado por cada servicio en el docker-compose
CMD ["uvicorn", "app.broker:app", "--host", "0.0.0.0", "--port", "8000"]
