#!/usr/bin/python3

"""
A class BaseModel that defines all common attributes/methods for other classes:
"""

import uuid
import datetime

class BaseModel:
    """
    A documentation of Public Instance Attributes:
    """
    
    def __init__(self, name):
        # Public instance attribute
        self.name = name

        # Assigning a unique id using uuid.uuid4() and converting it to a string
        self.id = str(uuid.uuid4())

        # Assigning created_at and updated_at with the current datetime
        current_datetime = datetime.utcnow()
        self.created_at = current_datetime
        self.updated_at = current_datetime

    def update_timestamp(self):
        # Updating the updated_at timestamp whenever the object is modified
        self.updated_at = datetime.utcnow()

