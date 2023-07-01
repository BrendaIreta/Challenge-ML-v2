from flask import Flask, request, redirect, url_for
import sqlite3
import requests

app = Flask(__name__)

class UserAuthentication:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def get_user_credentials(self):
        if not self.connection:
            raise Exception("No se ha establecido una conexión a la base de datos.")

        cursor = self.connection.cursor()
        cursor.execute("SELECT username, password FROM credenciales")

        return cursor.fetchall()

    def authenticate_user(self, form_username, form_password):
        user_credentials = self.get_user_credentials()

        for (username, password) in user_credentials:
            if username == form_username and password == form_password:
                return True

        return False
    
    def insert_data(self, data):
        if not self.connection:
            raise Exception("No se ha establecido una conexión a la base de datos.")

        cursor = self.connection.cursor()
        query = "INSERT INTO datos (campo1, campo2) VALUES (?, ?)"
        cursor.executemany(query, data)
        self.connection.commit()


db_connector = UserAuthentication("credenciales.sqlite")
db_connector.connect()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_username = request.form.get('username')
        form_password = request.form.get('password')

        if db_connector.authenticate_user(form_username, form_password):
            # Los datos coinciden, realizar acciones adicionales
            return redirect(url_for('success'))
        
        return "Credenciales inválidas"
     # Si el método de solicitud es GET, mostrar el formulario
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Nombre de usuario"><br>
            <input type="password" name="password" placeholder="Contraseña"><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    '''
@app.route('/success')
def success():
     # Obtener datos de la URL específica
    url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        db_connector.insert_data(data)
        return "Inicio de sesión exitoso. Datos insertados en la base de datos."
    else:
        return f"Error al obtener los datos. Código de estado: {response.status_code}"
