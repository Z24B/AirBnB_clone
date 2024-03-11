#!/usr/bin/python3
"""Defines class BaseModel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The base class for other classes"""

    def __init__(self, *args, **kwargs):
        """Initaliaze attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Override string representation of self"""
        fmt = self.__class__.__name__
        return "[{}] ({}) {}".format(fmt, self.id, self.__dict__)

    def save(self):
        """Updates last updated variable"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of self"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
