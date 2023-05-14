#!/usr/bin/python3
"""Test User module"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests methods and attributes in User class"""

    def test_init(self):
        """Test that a new User object is initialized correctly."""
        # check that User is a subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

        # check that the User class has the correct class attributes
        attrs = {
            "email": str,
            "password": str,
            "first_name": str,
            "last_name": str
        }

        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(User, attr_name))
            self.assertIsInstance(getattr(User, attr_name, None), attr_type)
