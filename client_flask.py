import requests

# Para tipos de peliculas
respuesta = requests.get(url='http://127.0.0.1:5000/type/all')
if respuesta.ok:
    print(respuesta.json())
else:
    print('No hay respuesta')

# Para tener lista de actores
respuesta = requests.get(url='http://127.0.0.1:5000/actors/all')
if respuesta.ok:
    print(respuesta.json())
else:
    print('No hay respuesta')