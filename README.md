# Challenge-ML-v2
El siguiente repositorio se divide en dos archivos principales.
apilogin.py
Desde este archivo se ejecutan las funciones principales:
1. Autenticar al usuario, encriptando y desencriptando sus credenciales.
2. Obtener la información y almacenarla encriptada.

Se requiere para su ejecución realizar las siguientes importaciones.
Importaciones: Importamos las clases Flask, request, jsonify, sqlalchemy y send_from_directory de la biblioteca Flask, 
así como el módulo requests para realizar solicitudes HTTP.

Rutas estáticas: Definimos una ruta /static/<path:path> que se utiliza para servir archivos estáticos.
La función serve_static() se encarga de devolver los archivos solicitados mediante la función send_from_directory().

Ruta principal: Definimos una ruta /static que se utiliza para servir los archivos:
index.html: Formulario de login
altausuario.html: Dar de alta a un usuario nuevo
exito.html: Sólo imprime un mensaje de éxito para indicar que los datos fueron insertados de forma correcta
dataurl.html: Ya desencriptados los datos los muestra en una página html

El siguiente archivo que complementa la api, es el que se encarga de crear la base de datos, utilizando SQLite, y SQLAlchemy
credenciales.sqlite y se ejecuta con la app mostrardata.py
Creación de engine: Requerido para que SQLAlchemy se comunique con la base de datos

Creación de sesión y los modelos: La cual se creo en el fichero db.py utilizando el método sessionmaker. Por medio de la clase Base se heredarán todos los modelos y tiene la capacidad de realizar el mapeo correspondiente a partir de la metainformación.

Modelos de la base de datos: Se encuentra en models.py, el cual contiene la estructura más básica para contener el username y password.

Y por último, la encriptación de los datos se realiza de forma manual, por medio de la aplicación genkey.py, se obtiene la llave para encriptar la información, la cual se debe sustituir en los archivos. donde se indica:
altausuario.py
apilogin.py
mostrardata.py

Los archivos que se seleccionaron para trabajar con esta api sólo fueron los que se enlistan a continuación:
    user_name, codigo_zip, credit_card_num, credit_card_cvv, cuenta_numero, direccion, foto_dni, ip, cantidad_compras_realizadas

