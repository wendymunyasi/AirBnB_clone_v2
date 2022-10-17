#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models.base_model import BaseModel, Base
# import json

from os import getenv

storage_env = getenv("HBNB_TYPE_STORAGE")
if storage_env == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
