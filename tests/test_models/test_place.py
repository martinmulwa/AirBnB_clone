#!/usr/bin/python3
"""Test Place module"""

import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """Tests methods and attributes in Place class"""

    def test_init(self):
        """Test that a new Place object is initialized correctly."""
        # check that Place is a subclass of BaseModel
        self.assertTrue(issubclass(Place, BaseModel))

        # check that the Place class has the correct class attributes
        attrs = {
            "city_id": str,
            "user_id": str,
            "name": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list
        }

        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(Place, attr_name))
            self.assertIsInstance(getattr(Place, attr_name, None), attr_type)
