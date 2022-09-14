#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base

# SQLAlchemy modules
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Defines a user

    Attributes:
        __tablename__ (str): Users MySQL table name

        email: (sqlalchemy String): User's email address column
        password (sqlalchemy String): User's password column
        first_name (sqlalchemy String): User's first name column
        last_name (sqlalchemy String): User's last name column
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Relatioships
    places = relationship("Place", backref="user", cascade="delete")
