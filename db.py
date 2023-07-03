from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Se crea una clase llamada base con el método declarative, la cual hereda todos los modelos
Base = declarative_base()
