import db

from sqlalchemy import Column, Integer, String, String


class Credenciales(db.Base):
    __tablename__ = 'credenciales'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'Credenciales({self.username}, {self.password})'

    def __str__(self):
        return self.username