#!/usr/bin/python3
"""Test Amenity module"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests methods and attributes in Amenity class"""

    def test_init(self):
        """Test that a new Amenity object is initialized correctly."""
        # check that Amenity is a subclass of BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))

        # check that the Amenity class has the correct class attributes
        attrs = {
            "name": str
        }

        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(Amenity, attr_name))
            self.assertIsInstance(getattr(Amenity, attr_name, None), attr_type)
