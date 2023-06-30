from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '0b378ffcc6b463e8b5aff7ef7c497d2e9d43c13850dcd2795682099637137421'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

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
    app.run()
