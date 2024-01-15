#!/usr/bin/python3
""" convert the dictionary representation to a JSON string"""
import datetime
import json
import os


class FileStorage:
    """serializes instances to a JSON file & deserializes JSON to instance"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key"""
        key = "{}.{}".format(type(obj).__name__. obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:

            dic = json.load(f)
            dic = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in dic.items()
                    }
            FileStorage.__objects = dic
