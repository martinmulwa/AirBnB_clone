#!/usr/bin/python3
"""Test City module"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests methods and attributes in City class"""

    def test_init(self):
        """Test that a new City object is initialized correctly."""
        # check that City is a subclass of BaseModel
        self.assertTrue(issubclass(City, BaseModel))

        # check that the City class has the correct class attributes
        attrs = {
            "name": str,
            "state_id": str
        }

        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(City, attr_name))
            self.assertIsInstance(getattr(City, attr_name, None), attr_type)
