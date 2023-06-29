import requests
import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='9sjA$*ba5eD7',
    database='extraccion_data_sensible'
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Obtener los datos de la API
url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
response = requests.get(url)
data = response.json()

# Recorrer los datos y realizar las inserciones en la base de datos
for usuario in data:
    # Obtener los valores de cada usuario
    nombre = usuario.get('user_name')
    zip = int(usuario.get('codigo_zip'))
    numerotarjeta = int(usuario.get('credit_card_num'))

    creartabla = '''
    CREATE TABLE clientes (
        nombre varchar (20),
        zip int primary key not null,
        numerotarjeta int primary key not null
    )
    '''

# Ejecutar la consulta para crear la tabla
    cursor.execute(creartabla)

    # Definir la consulta SQL para insertar los datos
    consulta = "INSERT INTO extraccion_data_sensible (nombre, zip, numerotarjeta) VALUES (%s, %s, %s)"

    # Datos a insertar en la tabla
    datos = (nombre, zip, numerotarjeta)

    # Ejecutar la consulta con los datos
    cursor.execute(consulta, datos)

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
