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
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
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
        """Retrieve all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
                cls.__name__,
                instance_id
                )

    @classmethod
    def destroy(cls, instance_id):
        """Deletes an instance"""
        return models.storage.delete_by_id(
                cls.__name__,
                instance_id
                )

    @classmethod
    def update(cls, instance_id, *args):
        """Updates an instance"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                    cls.__name__,
                    instance_id,
                    *arg
                    )


