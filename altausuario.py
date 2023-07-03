from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet

from db import Base
from models import Credenciales

altausuario = Flask(__name__)
engine = create_engine('sqlite:///credenciales.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Clave de encriptación (reemplazar por tu propia clave generada en genkey.py)
key = b'your-secret-key'
cipher_suite = Fernet(key)

@altausuario.route('/static')
def alta():
    return render_template('altausuario.html')


@altausuario.route('/static', methods=['POST'])
def guardar_credenciales():
    username = request.form['username']
    password = request.form['password']

    encrypted_password = cipher_suite.encrypt(password.encode()).decode()

    credencial = Credenciales(username, encrypted_password)
    session.add(credencial)
    session.commit()
    return 'Credenciales guardadas correctamente.'


if __name__ == '__main__':
    altausuario.run()




"""from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base
from models import Credenciales

altausuario = Flask(__name__)
engine = create_engine('sqlite:///credenciales.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@altausuario.route('/static')
def alta():
    return render_template('altausuario.html')


@altausuario.route('/static', methods=['POST'])
def guardar_credenciales():
    username = request.form['username']
    password = request.form['password']
    credencial = Credenciales(username, password)
    session.add(credencial)
    session.commit()
    return 'Credenciales guardadas correctamente.'

if __name__ == '__main__':
    altausuario.run()"""