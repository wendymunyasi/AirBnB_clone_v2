#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base

# SQLAlchemy modules
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float

class Place(BaseModel, Base):
    """ 
    Define a place

    Attributes:
        __tablename__ (str): Place MySQL table name

        city_id (sqlalchemy String): Place city id
        user_id (sqlalchemy String): Place user id
        name (sqlalchemy String): Place name
        description (sqlalchemy String): Place description
        number_rooms (sqlalchemy Integer): Place number of rooms
        number_bathrooms (sqlalchemy Integer): Placenumber of bathrooms
        max_guest (sqlalchemy Integer): Place maximum number of guests
        price_by_night (sqlalchemy Integer): Place price by night
        latitude (sqlalchemy Float): Place latitude
        longitude (sqlalchemy Float): Place  longitude
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    longitude = 0.0

    amenity_ids = []
