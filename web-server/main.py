import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creo mi primer API con Python:
app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,5]

@app.get('/contact')
def get_contact():
    return {"name": 'Gobea & Co',
            "president" : "Mariano Gobea Alcoba"}

@app.get('/test_html', response_class=HTMLResponse)
def get_html():
    return """
    <h1>Hola soy una pagina<h1>
    <p>Soy un parrafo<p>
    """

def run():
    store.get_categories()

if __name__ == "__main__":
    run()