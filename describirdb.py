import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='9sjA$*ba5eD7',
    database='extraccion_data_sensible'
)

# Cerrar el cursor y la conexión
conexion.close()
