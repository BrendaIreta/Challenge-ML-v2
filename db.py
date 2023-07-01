from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///credenciales.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

#Se crea una clase llamada base con el método declarative, la cual hereda todos los modelos
Base = declarative_base()
