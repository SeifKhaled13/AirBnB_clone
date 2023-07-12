#!/usr/bin/python3
"""define base model class"""
import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""
    def __init__(self):
        """Initializes a new base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """Returns a dictionary for keys/values of __dict__ of instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"