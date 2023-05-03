# Declaro la versión de python que voy a usar en el proyecto:
FROM python:3.10

# Creo una carpeta raiz para el espacio de trabajo
WORKDIR /app
# Le indico cque me genere el archivo requirements.txt dentro de la carpeta raiz
COPY requirements.txt /app/requirements.txt

# Le digo que directamente me instale las dependencias que están en requirementes
# que no instale desde el cahce y que actualice lo que tenga que actualizar. 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiamos todo nuestro espacio de trabajo a la carpeta raiz
COPY . /app/

# Agrego un comando que va a encender el servidor de Uvicorn:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]