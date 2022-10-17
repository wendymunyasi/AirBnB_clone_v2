#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a list of objects of one type of class.

        Args:
            cls (any, optional): Class of object. Defaults to None.

        Returns:
            list: list of objects of one type of class.
        """
        if cls is None:
            return FileStorage.__objects
        return {
            key: value for key, value in self.__objects.items()
            if type(value) is cls
        }

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects

        If obj is equal to None, the method should not do anything.
        Args:
            obj (models.class.<any model>, optional): object to delete.
            Defaults to None.
        """
        if obj in self.__objects.values():
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del(self.__objects[key])
        return

    def close(self):
        """Calls reload method for deserializing the JSON file to objects
        """
        self.reload()
