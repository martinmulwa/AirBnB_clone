#!/usr/bin/python3
"""Test FileStorage module."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """Test methods and attributes in FileStorage class."""

    def test_init(self):
        """Test that FileStorage objects are initialized correctly."""
        # check that FileStorage has __file_path private class attribute
        self.assertIsNotNone(FileStorage._FileStorage__file_path)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

        # check that FileStorage has __objects private class attribute
        self.assertIsNotNone(FileStorage._FileStorage__objects)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """Test 'all' method of FileStorage objects."""
        fs = FileStorage()
        self.assertIs(fs.all(), FileStorage._FileStorage__objects)

    def test_new(self):
        """Test 'new' method of FileStorage objects."""
        fs = FileStorage()

        # create new BaseModel object and check that it's not in __objects
        bm = BaseModel()
        bm_key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertTrue(bm_key not in FileStorage._FileStorage__objects)

        # add the BaseModel object to __objects and check that it was added
        fs.new(bm)
        self.assertTrue(bm_key in FileStorage._FileStorage__objects)
        self.assertIs(bm, FileStorage._FileStorage__objects[bm_key])
