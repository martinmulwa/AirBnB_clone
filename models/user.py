#!/usr/bin/python3
"""User module."""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes and methods for User objects."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
