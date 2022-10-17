#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

import models
from models.amenity import Amenity
from models.base_model import Base, BaseModel

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', ondelete='CASCADE'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id',
                                            ondelete='CASCADE'),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """
    Define a place

    Attributes:
        __tablename__ (str): Place MySQL table name

        city_id (string): id of city.
        user_id (string): id of user.
        name (string): name of Place.
        description (string): description of place.
        number_rooms (integer): number of rooms in place.
        number_bathrooms (integer): number of bathrooms in place.
        max_guest (integer): maximum number of guests allowed in a place.
        price_by_night (integer): price of room per night.
        latitude (float): latitude of place on a map.
        longitude (float): longitude of place on a map.
        amenity_ids (list (of string)): list of Amenity.id of place.
    """

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id",
                         ondelete='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id",
                         ondelete='CASCADE'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan',
                               passive_deletes=True)
        amenities = relationship('Amenity', backref='place_amenities',
                                 cascade='all, delete',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 passive_deletes=True)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to
            the current Place.id.

            Returns:
                list: a list of review instances.
            """
            from models.review import Review
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place.

            Returns:
                list: list of amenity instances.
            """
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """Handles append method for adding an Amenity.id to the attribute
            amenity_ids. This method should accept only Amenity object,
            otherwise, do nothing.
            """
            if not isinstance(obj, Amenity):
                return
            self.amenity_ids.append(obj.id)
