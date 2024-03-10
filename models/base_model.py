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
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid4())
            self.id = kwargs['id']
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(
                        kwargs['created_at'],
                        '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.utcnow()
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(
                        kwargs['updated_at'],
                        '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """Override string representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """Updates last updated variable"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of self"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Returns a dictionary of all instances of the class."""
        from models import storage
        return {k: v for k, v in storage.all().items() if isinstance(v, cls)}

    @classmethod
    def count(cls):
        """Returns the number of instances of the class."""
        from models import storage
        return len([    obj for obj in storage.all().values() if isinstance(obj, cls)])
