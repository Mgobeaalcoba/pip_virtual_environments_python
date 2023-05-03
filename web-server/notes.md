## Levantando un servidor rapidamente con FastAPI

1- Instalo en mi proyecto FastAPI & Uvicorn:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

2- Levanto en mi archivo main.py o el que nombre que desee y luego ejecute un servidor. Por ejemplo, este: 

```python
from fastapi import FastAPI

# Creo mi primer API con Python:
app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,5]

@app.get('/contact')
def get_contact():
    return {"name": 'Gobea & Co',
            "president" : "Mariano Gobea Alcoba"}
```

3- Levanto mi servidor para que esté escuchando en la web o en algún puerto de mi PC con uvicorn:

```bash
uvicorn main:app --reload
```

main es el nombre del archivo y app es el nombre de la instancia de FastAPI creada. 

4- Listo puedo pegarle al puerto que uvicorn me indica para obtener las respuestas de mis request de tipo GET que programé arriba. 

-----------------------

FastAPI también sirve con su paquete HTMLResponse para retornar un HTML a la request que le hagamos. Ejemplo: 

```python
from fastapi import FastAPI

# Creo mi primer API con Python:
app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,5]

@app.get('/contact')
def get_contact():
    return {"name": 'Gobea & Co',
            "president" : "Mariano Gobea Alcoba"}
```