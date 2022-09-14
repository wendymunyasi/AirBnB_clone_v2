#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
import json
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    attributeibutes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes new instances of DBStorage.
        """
        try:
            user = os.environ.get('HBNB_MYSQL_USER')
            password = os.environ.get('HBNB_MYSQL_PWD')
            host = os.environ.get('HBNB_MYSQL_HOST')
            db = os.environ.get('HBNB_MYSQL_DB')
            env = os.environ.get('HBNB_ENV')
            attributes = [user, password, host, db]
            for attribute in attributes:
                if attribute is None:
                    print("Missing attributes env var")

            conn_str = "mysql+mysqldb://{}:{}@{}/{}".format(
                        user, password, host, db)
            # create engine and session object with connection string
            self.__engine = create_engine(conn_str, pool_pre_ping=True)

            # drop all tables in DB if test env
            if env == 'test':
                Base.metadata.drop_all(bind=self.__engine, checkfirst=True)
        except Exception as E:
            print("raised exception in init")
            print(E)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects
        epending of the class name (argument cls).

        key = <class-name>.<object-id>
        value = object

        Args:
            cls (any, optional): class. Defaults to None.

        Returns:
            dict: al objects
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """adds the object to the current database session (self.__session)
        therefore sets __object to given obj.

        Args:
            obj: given object
        """
        if obj and self.__session:
            self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session
        (self.__session).
        """
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """deletes obj if not none from the current database session
        (__objects).
        """
        try:
            self.__session.delete(obj)
        except Exception:
            pass

    def reload(self):
        """creates all tables in the database (feature of SQLAlchemy).

        (WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine)).
        Creates the current database session (self.__session) from the
        engine (self.__engine) by using a sessionmaker - the option
        expire_on_commit must be set to False ; and scoped_session - to
        make sure your Session is thread-safe.
        """
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            self.__session = scoped_session(session_factory)
        except Exception as E:
            print(E)

    def close(self):
        """removes our session"""
        self.__session.remove()
