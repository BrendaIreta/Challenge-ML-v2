# Challenge-ML-v2
El siguiente repositorio se divide en dos archivos principales.
apilogin.py
Importaciones: Importamos las clases Flask, request, jsonify y send_from_directory de la biblioteca Flask, 
así como el módulo requests para realizar solicitudes HTTP.

Creación de la aplicación: Creamos una instancia de la clase Flask y la asignamos a la variable app. El parámetro __name__ 
se utiliza para indicar el nombre del módulo actual.

Rutas estáticas: Definimos una ruta /static/<path:path> que se utiliza para servir archivos estáticos.
La función serve_static() se encarga de devolver los archivos solicitados mediante la función send_from_directory().

Ruta principal: Definimos una ruta / que se utiliza para servir el archivo index.html. La función serve_index() 
devuelve el archivo index.html mediante la función send_from_directory().

Ruta de datos: Definimos una ruta /datos con el método POST para recibir datos del formulario. 
Extraemos los valores de username y password del formulario utilizando request.form.get(). Luego, verificamos si las credenciales son válidas realizando una autenticación básica. Si las credenciales son válidas, realizamos una solicitud HTTP a la URL especificada y devolvemos los datos obtenidos en formato JSON. Si las credenciales son inválidas, devolvemos un mensaje de error.

Ejecución de la aplicación: Finalmente, verificamos si el archivo se está ejecutando directamente (__name__ == '__main__') y 
ejecutamos la aplicación Flask utilizando el método run(). Además, se habilita el contexto de SSL ad-hoc para ejecutar 
el servidor en modo de depuración (debug=True).

El siguiente archivo que complementa la api, es el que se encarga de crear la base de datos, utilizando SQLite, y SQLAlchemy
credenciales.sqlite y se ejecuta con el main.py
Creación de engine: Requerido para que SQLAlchemy se comunique con la base de datos

Creación de sesión y los modelos: La cual se ccreo en el fichero bd.py utilizando el método sessionmaker. Por medio de la clase
Base se heredarán todos los modelos y tiene la capacidad de realizar el mapeo correspondiente a partir de la metainformación.

Modelos de la base de datos: Se encuentra en models.py, el cual contiene la estructura más básica para contener el username y password


