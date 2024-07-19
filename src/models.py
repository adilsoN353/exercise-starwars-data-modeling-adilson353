import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    # First_name = Column(String(250), nullable=True)
    Last_name = Column(String(250), nullable=True)
    user_name = Column(String(250), nullable= True)
    email = Column(String(300), nullable=True)
    is_active = Column(Boolean(),unique = False , nullable = False)
    favorites = relationship ("Favorites", backref = "user", lazy = True) 

    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    favorites = relationship ("Favorites", backref = "user", lazy = True)


    diameter = Column(String(250), nullable = False) 
    rotation_period = Column(String(250), nullable = False) 
    orbital_period = Column(String(250), nullable = False) 
    gravity = Column(String(250), nullable = False) 
    population = Column(String(250), nullable = False) 
    climate = Column(String(250), nullable = False) 


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer , ForeignKey("planet.id"))
    starships_id = Column(Integer , ForeignKey("starships.id"))
    characters_id = Column(Integer , ForeignKey("characters.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    favorites = relationship ("Favorites", backref = "user", lazy = True)

    model = Column(String(250), nullable = False) 
    starship_class = Column(String(250), nullable = False) 
    manufacturer = Column(String(250), nullable = False) 
    cost_in_credits = Column(String(250), nullable = False) 
    length = Column(String(250), nullable = False) 
    crew = Column(String(250), nullable = False) 
    passengers = Column(String(250), nullable = False) 



class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    favorites = relationship ("Favorites", backref = "user", lazy = True)

    height =  Column(String(250), nullable = False) 
    mass =  Column(String(250), nullable = False) 
    hair_color =  Column(String(250), nullable = False) 
    skin_color =  Column(String(250), nullable = False) 
    eye_color =  Column(String(250), nullable = False) 
    birth_year =  Column(String(250), nullable = False) 
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
