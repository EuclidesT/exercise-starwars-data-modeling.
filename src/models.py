import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    date = Column(Date, index=True)

    def to_dict(self):
        return {}
    
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    altura = Column(Float, nullable=False)
    peso = Column(Float, nullable=False)
    unidades_altura = Column(String(250), nullable=False)
    unidades_peso = Column(String(250), nullable=False)


    def to_dict(self):
        return {}
    
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    poblacion = Column(Integer, nullable=False)
    periodo_rotacion = Column(Integer, nullable=False)
    supercie_agua = Column(Integer, nullable=False)
    diametro = Column(Integer, nullable=False)

    def to_dict(self):
        return {}
    
class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    marca = Column(String(250), nullable=False)
    capacidad = Column(Integer, nullable=False)
    personaje = Column(Integer, nullable=False)
    modelo = Column(String(250), nullable=False)
    tripulacion = Column(Integer, nullable=False)

    def to_dict(self):
        return {}
    
class Peliculas(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    año = Column(Date, index=True)
    director = Column(String(250), ForeignKey('director.id'))
    duracion = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    edad = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}
    
class Favorite_Planeta(Base):
    __tablename__ = 'favorite_planeta'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    planeta = Column(Integer, ForeignKey('planeta.id'))

    def to_dict(self):
        return {}
    
class Favorite_Vehiculo(Base):
    __tablename__ = 'favorite_vehiculo'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))   
    vehiculo = Column(Integer, ForeignKey('vehiculo.id'))

    def to_dict(self):
        return {}
    
class Favorite_Personaje(Base):
    __tablename__ = 'favorite_personaje'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))   
    Personaje = Column(Integer, ForeignKey('personaje.id'))

    def to_dict(self):
        return {}
    
class Favorite_Pelicula(Base):
    __tablename__ = 'favorite_pelicula'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('peliculas.id'))   
    pelicula = Column(Integer, ForeignKey('peliculas.id'))

    def to_dict(self):
        return {}
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
