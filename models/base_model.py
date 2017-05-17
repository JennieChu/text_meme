#!/usr/bin/python3
"""
This module contains the BaseModel class, that all other classes inherit from
"""
from datetime import datetime
import models
from os import getenv
from sqlalchemy import Column, Integer, String, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel:
    """BaseModel to be inherited for all objects"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.now(),
                        nullable=False, onupdate=datetime.now)

    def __init__(self, *args, **kwargs):
        """
        Initialize class
        """
        if args:
            kwargs = args[0]
        if kwargs:
            flag_id = False
            flag_created_at = False
            for k in kwargs.keys():
                if k == "created_at" or k == "updated_at":
                    if k == "created_at":
                        flag_created_at = True
                    if not instance(kwargs[k], datetime):
                        kwargs[k] = datetime(*self.__str_to_numbers(kwargs[k]))
                elif k == "id":
                    flag_id = True
                setattr(self, k, kwargs[k])
            if not flag_created_at:
                self.created_at = datetime.now()
            if not flag_id:
                self.id = str(uuid.uuid4())
        elif not args:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())

    def __str_to_numbers(self, s):
        """
        Prepares a string for datetime
        """
        tmp = ''.join([o if o not in "T;:.,-_" else " " for o in s]).split()
        res = [int(i) for i in tmp]
        return res

    def save(self):
        """
        method to save model
        """
        self.__dict__["updated_at"] = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__ (self):
        """
        format string representation
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def to_json(self, saving=False):
        """
        convert file to json
        """
        dupe = self.__dict__.copy()
        dupe.pop('_sa_instance_state', None)

        dupe["created_at"] = dupe["created_at"].isoformat()
        if ("updated_at" in dupe):
            dupe["updated_at"] = dupe["created_at"].isoformat()
        dupe["__class__"] = type(self).__name__
        if not saving:
            dupe.pop("password", None)
        dupe.pop("amenities", None)
        dupe.pop("amenities_id", None)
        return dupe
