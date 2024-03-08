#!/usr/bin/python3
"""Defines class BaseModel"""
import models
import uuid
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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def all(cls):
        """Returns a dictionary of all instances of the class."""
        from models import storage
        return {k: v for k, v in storage.all().items() if isinstance(v, cls)}

    @classmethod
    def count(cls):
        """Returns the number of instances of the class."""
        from models import storage
        return len([obj for obj in storage.all().values() if isinstance(obj, cls)])
