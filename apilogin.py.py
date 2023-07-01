from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Ruta para servir archivos estáticos
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Ruta para servir el archivo index.html
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')



@app.route('/datos', methods=['POST'])
def obtener_datos():
    username = request.form.get('username')
    password = request.form.get('password')

    # Realizar la autenticación verificando el usuario y contraseña
    if username == 'admin' and password == 'password':
        # Si las credenciales son válidas, realizar la solicitud HTTP a la URL
        url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data), 200
        else:
            return jsonify({'message': 'Error al obtener los datos'}), response.status_code
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True)
