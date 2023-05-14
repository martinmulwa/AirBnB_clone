#!/usr/bin/python3
"""Test Review module"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests methods and attributes in Review class"""

    def test_init(self):
        """Test that a new Review object is initialized correctly."""
        # check that Review is a subclass of BaseModel
        self.assertTrue(issubclass(Review, BaseModel))

        # check that the Review class has the correct class attributes
        attrs = {
            "place_id": str,
            "user_id": str,
            "text": str
        }

        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(Review, attr_name))
            self.assertIsInstance(getattr(Review, attr_name, None), attr_type)
