#!/usr/bin/python3
"""Defines class BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The base class for other classes"""
    def __init__(self, *args, **kwargs):
        """Initaliaze attributes"""
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, timeform)
                setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.today())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.today())

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    @classmethod
    def all(cls):
        """Returns a dictionary of all instances of the class."""
        from models import storage
        return {k: v for k, v in storage.all().items() if isinstance(v, cls)}

    @classmethod
    def count(cls):
        """Returns the number of instances of the class."""
        from models import storage
        return len([
            obj for obj in storage.all().values() if isinstance(obj, cls)])
