#!/usr/bin/python3
"""Defines class FileStorage"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                loaded_objects = json.load(f)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    class_name = eval(class_name)
                    self.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass
