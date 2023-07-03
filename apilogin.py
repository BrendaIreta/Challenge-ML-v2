from flask import Flask, request, redirect, url_for
from sqlalchemy import create_engine, Column, String, Float, Integer
from db import Base
from sqlalchemy.orm import sessionmaker
import requests
from cryptography.fernet import Fernet

app = Flask(__name__)
key = b'your-secret-key'  # Clave de encriptación (reemplazar por tu propia clave generada en genkey.py)
cipher_suite = Fernet(key)

class Credenciales(Base):
    __tablename__ = 'credenciales'
    username = Column(String, primary_key=True)
    password = Column(String)

    def decrypt_password(self):
        decrypted_password = cipher_suite.decrypt(self.password.encode()).decode()
        return decrypted_password

class DatosURL(Base):
    __tablename__ = 'datosurl'
    id = Column(String, primary_key=True)
    user_name = Column(String)
    codigo_zip = Column(String)
    credit_card_num = Column(Integer)
    credit_card_cvv = Column(Integer)
    cuenta_numero = Column(Integer)
    direccion = Column(String)
    cuenta_numero = Column(Integer)
    direccion = Column(String)
    foto_dni = Column(String)
    ip = Column(Float)
    cantidad_compras_realizadas = Column(Integer)

    def encrypt_data(self):
        encrypted_data = {}
        encrypted_data['id'] = cipher_suite.encrypt(self.id.encode()).decode()
        encrypted_data['user_name'] = cipher_suite.encrypt(self.user_name.encode()).decode()
        encrypted_data['codigo_zip'] = cipher_suite.encrypt(self.codigo_zip.encode()).decode()
        encrypted_data['credit_card_num'] = cipher_suite.encrypt(self.credit_card_num.encode()).decode()
        encrypted_data['credit_card_cvv'] = cipher_suite.encrypt(self.credit_card_cvv.encode()).decode()
        encrypted_data['cuenta_numero'] = cipher_suite.encrypt(self.cuenta_numero.encode()).decode()
        encrypted_data['direccion'] = cipher_suite.encrypt(self.direccion.encode()).decode()
        encrypted_data['foto_dni'] = cipher_suite.encrypt(self.foto_dni.encode()).decode()
        encrypted_data['ip'] = cipher_suite.encrypt(self.ip.encode()).decode()
        encrypted_data['cantidad_compras_realizadas'] = cipher_suite.encrypt(self.cantidad_compras_realizadas.encode()).decode()
        return encrypted_data
    
class UserAuthentication:
    def __init__(self, db_file):
        self.db_file = db_file
        self.engine = None
        self.session = None

    def connect(self):
        self.engine = create_engine('sqlite:///' + self.db_file)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def disconnect(self):
        if self.session:
            self.session.close()

    def get_user_credentials(self):
        return self.session.query(Credenciales).all()

    def authenticate_user(self, form_username, form_password):
        user_credentials = self.get_user_credentials()

        for user in user_credentials:
            if user.username == form_username and user.decrypt_password() == form_password:
                return True

        return False

    def insert_data(self, data):
        for usuario in data:
            datos_url = DatosURL(
                id=self.encrypt_field(usuario['id']),
                user_name=self.encrypt_field(usuario['user_name']),
                codigo_zip=self.encrypt_field(usuario['codigo_zip'])
                credit_card_num=self.encrypt_field(usuario['credit_card_num'])
                credit_card_cvv=self.encrypt_field(usuario['credit_card_cvv'])
                cuenta_numero=self.encrypt_field(usuario['cuenta_numero'])
                direccion=self.encrypt_field(usuario['direccion'])
                foto_dni=self.encrypt_field(usuario['foto_dni'])
                ip=self.encrypt_field(usuario['ip'])
                cantidad_compras_realizadas=self.encrypt_field(usuario['cantidad_compras_realizadas'])
            )

            encrypted_data = datos_url.encrypt_data()
            datos_url.id = encrypted_data['id']
            datos_url.user_name = encrypted_data['user_name']
            datos_url.codigo_zip = encrypted_data['codigo_zip']
            datos_url.credit_card_num = encrypted_data['credit_card_num']
            datos_url.credit_card_cvv = encrypted_data['credit_card_cvv']
            datos_url.cuenta_numero = encrypted_data['cuenta_numero']
            datos_url.direccion = encrypted_data['direccion']
            datos_url.foto_dni = encrypted_data['foto_dni']
            datos_url.ip = encrypted_data['ip']
            datos_url.cantidad_compras_realizadas = encrypted_data['cantidad_compras_realizadas']
            self.session.add(datos_url)

        self.session.commit()

db_connector = UserAuthentication("credenciales.sqlite")
db_connector.connect()

@app.route('/static', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_username = request.form.get('username')
        form_password = request.form.get('password')

        if db_connector.authenticate_user(form_username, form_password):
            # Los datos coinciden
            return redirect(url_for('success'))
        
        return "Credenciales inválidas"
    
    # Si el método de solicitud es GET, mostrar el formulario
    return app.send_static_file('index.html')

@app.route('/static')
def success():
    # Obtener datos de la URL específica
    url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        db_connector.insert_data(data)
        return redirect(url_for('exito'))  # Redirigir a la ruta '/static/exito'
    else:
        return f"Error al obtener los datos. Código de estado: {response.status_code}"
    
@app.route('/static/exito')
def exito():
    return app.send_static_file('exito.html')


if __name__ == '__main__':
    app.run()

