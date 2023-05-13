#!/usr/bin/python3
"""Test FileStorage module."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """Test methods and attributes in FileStorage class."""

    @classmethod
    def setUpClass(cls):
        cls.file_path = "test_file.json"

        # remove file_path if it exists
        if os.path.exists(cls.file_path):
            try:
                os.remove(cls.file_path)
            except Exception:
                raise Exception(f"Error: Could not remove {cls.file_path}")

        FileStorage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        # remove file_path if it exists
        if os.path.exists(cls.file_path):
            try:
                os.remove(cls.file_path)
            except Exception:
                raise Exception(f"Error: Could not remove {cls.file_path}")

    def setUp(self):
        """Create FileStorage object for testing."""
        self.fs = FileStorage()

    def test_init(self):
        """Test that FileStorage objects are initialized correctly."""
        # check that FileStorage has __file_path private class attribute
        self.assertIsNotNone(FileStorage._FileStorage__file_path)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

        # check that FileStorage has __objects private class attribute
        self.assertIsNotNone(FileStorage._FileStorage__objects)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all(self):
        """Test 'all' method of FileStorage class."""
        self.assertIs(self.fs.all(), FileStorage._FileStorage__objects)

    def test_new(self):
        """Test 'new' method of FileStorage class."""
        # create new BaseModel object and check that it's not in __objects
        bm = BaseModel()
        bm_key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertTrue(bm_key not in FileStorage._FileStorage__objects)

        # add the BaseModel object to __objects and check that it was added
        self.fs.new(bm)
        self.assertTrue(bm_key in FileStorage._FileStorage__objects)
        self.assertIs(bm, FileStorage._FileStorage__objects[bm_key])

    def test_save(self):
        """Test 'save' method of FileStorage class."""
        file_path = FileStorage._FileStorage__file_path

        # remove file_path if it exists
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                raise Exception(f"Error: Could not remove {file_path}")

        # check that file_path doesn't exist
        self.assertFalse(os.path.exists(file_path))

        self.fs.save()

        # check that file_path exists
        self.assertTrue(os.path.exists(file_path))
