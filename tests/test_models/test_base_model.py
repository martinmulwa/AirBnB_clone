#!/usr/bin/python3
"""Test Base Model module."""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test methods and attributes in BaseModel."""

    def setUp(self):
        """Create BaseModel objects for testing."""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_init(self):
        """Test that BaseModel objects are initialized correctly."""
        # create BaseModel objects for testing

        # check that id attribute is a string
        self.assertIs(type(self.bm1.id), str)

        # check that id attribute is unique
        self.assertNotEqual(self.bm1.id, self.bm2.id)

        # check that created_at and updated_at attributes are datetime objects
        self.assertIsInstance(self.bm1.created_at, datetime.datetime)
        self.assertIsInstance(self.bm1.updated_at, datetime.datetime)

        # check that created_at and updated_at attributes are equal
        self.assertIsNot(self.bm1.created_at, self.bm1.updated_at)
        self.assertEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_str(self):
        """Test string representation of BaseModel objects."""
        bm1_str = (
            f"[{type(self.bm1).__name__}] "
            + f"({self.bm1.id}) "
            + f"{self.bm1.__dict__}"
        )

        self.assertEqual(bm1_str, str(self.bm1))

    def test_save(self):
        """Test save method of BaseModel objects."""
        updated_before = self.bm2.updated_at
        self.bm2.save()
        updated_after = self.bm2.updated_at

        self.assertGreater(updated_after, updated_before)

    def test_to_dict(self):
        """Test to_dict method of BaseModel objects."""
        bm2_dict = dict(self.bm2.__dict__)

        bm2_dict["__class__"] = type(self.bm2).__name__
        bm2_dict["created_at"] = self.bm2.created_at.isoformat()
        bm2_dict["updated_at"] = self.bm2.updated_at.isoformat()

        self.assertEqual(bm2_dict, self.bm2.to_dict())
