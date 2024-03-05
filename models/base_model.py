#!/usr/bin/python3
"""Defines class BaseModel"""
from models import storage
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
            storage.new(self)

    def __str__(self):
        """Return string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
