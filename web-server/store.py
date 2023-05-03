import requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories'


def get_categories():
    r = requests.get(api_url_categories)
    print(f'Status code: {r.status_code}')
    # print(f'Text: {r.text}')
    print(type(r.text))
    # Transformo mi respuesta de la API de tipo string a JSON.
    categories = r.json()
    # Esto convierte mi respuesta en una lista de diccionarios. Por lo que puedo 
    # iterarlo con un for por ejemplo. 
    print()
    # print(categories)
    print(type(categories))
    print()

    for category in categories:
        print(category['name'])