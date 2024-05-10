#!/usr/bin/python3

"""
A class BaseModel that defines all common attributes/methods for other classes:
"""

from .. import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A  Public Instance Attributes:
    """
    def __init__(self, name):
        # Public instance attribute
        self.name = name

        # Assigning a unique id and converting it to a string
        self.id = str(uuid4())

        # Assigning created_at and updated_at with the current datetime
        current_datetime = datetime.datetime.now()
        self.created_at = current_datetime
        self.updated_at = current_datetime

    def update_timestamp(self):
        # Updating the updated_at timestamp whenever the object is modified
        self.updated_at = datetime.datetime.now()

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    """
     A documentation of Public instance methods:
    """

    def __init__(self, name):
        # Public instance method
        self.name = name

    def save(self):
        # Public instance method to update the public instance attribute
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        # A pubic instance method to return a dictionary
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
