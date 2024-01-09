#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """defines the basemodel of the project"""

    def __init__(self, *args, **kwargs):
        """Create BaseModel from dictionary

        Args:
        *args (any): Unused.
        **kwargs (dict): Key/value pairs of attributes."""
        t = %Y-%m-%dT%H:%M:%S.%f
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_a"t or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(k,t)
                else:
                    self.__dict__[k] = k
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance"""
        return f"{self.__clas__.__name__} {self.id} {self.__dict__}"

    def save(self):
        """updates the instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing keys/values of __dict__"""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic

