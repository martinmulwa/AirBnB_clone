#!/usr/bin/python3
"""Test Base Model module."""

from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Test methods and attributes in BaseModel."""

    def setUp(self):
        """Create BaseModel objects for testing."""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_init(self):
        """Test that BaseModel objects are initialized correctly."""
        # create BaseModel objects for testing

        # check that a BaseModel object has an id attribute which is a string
        self.assertIsNotNone(self.bm1.id)
        self.assertIs(type(self.bm1.id), str)

        # check that id attribute is unique
        self.assertNotEqual(self.bm1.id, self.bm2.id)

        # check that created_at and updated_at attributes are datetime objects
        self.assertIsNotNone(self.bm1.created_at)
        self.assertIsNotNone(self.bm1.updated_at)
        self.assertIsInstance(self.bm1.created_at, datetime)
        self.assertIsInstance(self.bm1.updated_at, datetime)

        # check that created_at and updated_at attributes are equal
        self.assertIsNot(self.bm1.created_at, self.bm1.updated_at)
        self.assertEqual(self.bm1.created_at, self.bm1.updated_at)

        # test __init__ with valid kwargs
        model_json = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model",
        }

        bm3 = BaseModel(**model_json)

        created_at = datetime.fromisoformat(model_json["created_at"])
        updated_at = datetime.fromisoformat(model_json["updated_at"])
        model_json["created_at"] = created_at
        model_json["updated_at"] = updated_at

        for key, value in model_json.items():
            if key not in ["__class__"]:
                self.assertEqual(getattr(bm3, key, None), value)

        # test __init__ with invalid kwargs
        model_json_invalid = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model",
        }

        with self.assertRaises(TypeError):
            bm3 = BaseModel(**model_json_invalid)

        # test __init__ with invalid kwargs
        model_json_missing = {
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model",
        }

        with self.assertRaises(TypeError):
            bm3 = BaseModel(**model_json_missing)

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
