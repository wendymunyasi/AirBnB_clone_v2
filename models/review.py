#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
# SQLAlchemy modules
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Review(BaseModel, Base):
    """ Defines a class Review

    Attributes:
        __tablename__ (str): reviews

        place_id (string): id of place.
        user_id (string): id of user.
        text (string): just a text.
    """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    # place_id = ""
    # user_id = ""
    # text = ""
