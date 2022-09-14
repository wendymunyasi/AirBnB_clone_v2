#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# SQLAlchemy modules
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Amenity(BaseModel, Base):
    """Defines a class Amenity

    Attributes:
        __tablename__ (str): amenities

        name (str): name of amenity.
    """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
