#!/usr/bin/python3
"""BaseModel module."""

from datetime import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel object with given attributes."""

        # if kwargs is provided and is not empty
        if kwargs and len(kwargs):
            # check that no required kwargs are missing
            required_kwargs = ["id", "created_at", "updated_at", "__class__"]

            excluded_kwargs = ["created_at", "updated_at", "__class__"]

            for key in required_kwargs:
                if key not in kwargs:
                    raise TypeError(f"Missing Attribute Argument: {key}")

            # check if the given kwargs are invalid
            try:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            except ValueError:
                raise TypeError("Invalid Attribute Argument: created_at")

            try:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
            except ValueError:
                raise TypeError("Invalid Attribute Argument: updated_at")

            # create attributes for the BaseModel object using the kwargs
            for key, value in kwargs.items():
                if key not in excluded_kwargs:
                    setattr(self, key, value)

        # if kwargs is not provided or is empty
        else:
            self.id = str(uuid.uuid4())

            now = datetime.now()
            self.created_at = now

            # create copy of now datetime object
            self.updated_at = datetime(
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.second,
                now.microsecond,
            )

    def __str__(self):
        """Return unofficial string representation of a BaseModel object"""
        class_name = self.__class__.__name__

        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing attributes of BaseModel object."""
        bm_dict = self.__dict__

        class_name = self.__class__.__name__
        created_at = self.created_at.isoformat()
        updated_at = self.updated_at.isoformat()

        bm_dict["__class__"] = class_name
        bm_dict["created_at"] = created_at
        bm_dict["updated_at"] = updated_at

        return bm_dict
