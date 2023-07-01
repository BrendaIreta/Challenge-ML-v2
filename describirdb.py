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

# Insertar datos en el campo 'nombre'
nombre = 'John Doe'
consulta_insertar = "INSERT INTO clientes2 (nombre) VALUES (%s)"
datos_insertar = (nombre,)
cursor.execute(consulta_insertar, datos_insertar)

# Confirmar los cambios en la base de datos
conexion.commit()

# Leer datos del campo 'nombre'
consulta_leer = "SELECT nombre FROM clientes2"
cursor.execute(consulta_leer)

# Obtener los resultados y mostrar los datos
resultados = cursor.fetchall()
print("Datos del campo 'nombre':")
for resultado in resultados:
    print(resultado[0])

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
