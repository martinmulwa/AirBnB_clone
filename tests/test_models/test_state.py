#!/usr/bin/python3
"""Test State module"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """Tests methods and attributes in State class"""

    def test_init(self):
        """Test that a new State object is initialized correctly."""
        # check that State is a subclass of BaseModel
        self.assertTrue(issubclass(State, BaseModel))

        # check that the State class has the correct class attributes
        attrs = {
            "name": str
        }

        for attr_name, attr_type in attrs.items():
            self.assertTrue(hasattr(State, attr_name))
            self.assertIsInstance(getattr(State, attr_name, None), attr_type)
