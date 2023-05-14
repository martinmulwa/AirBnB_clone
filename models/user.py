#!/usr/bin/python3
"""inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
