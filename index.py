import requests
url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for usuario in data:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['user_name']}")
        print(f"Código ZIP:: {usuario['codigo_zip']}")
        print("-----")
else:
    print(f"Error al obtener los datos. Código de estado: {response.status_code}")