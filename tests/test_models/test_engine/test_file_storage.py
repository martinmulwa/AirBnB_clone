#!/usr/bin/python3
"""Test FileStorage module."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test methods and attributes in FileStorage class."""

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
        file_path = "../../../models/engine/" + file_path
        objects = FileStorage._FileStorage__objects

        # add new objects to objects dict and save to file storage
        bm1 = BaseModel()
        bm2 = BaseModel()

        for bm in [bm1, bm2]:
            bm_key = f"{bm.__class__.__name__}.{bm.id}"
            objects[bm_key] = bm

        self.fs.save()

        # check that file_path exists
        self.assertTrue(os.path.exists(file_path))

        # read content of file_path and check it's the same as objects
        with open(file_path, "r") as f:
            # Load the contents of the file as a dictionary
            file_dict = json.load(f)
            self.assertEqual(file_dict, objects)
