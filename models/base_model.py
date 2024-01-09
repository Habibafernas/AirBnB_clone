#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""


class BaseModel:
    """defines the basemodel of the project"""

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

