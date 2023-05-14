#!/usr/bin/python3
"""Test FileStorage module."""

import os
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test methods and attributes in FileStorage class."""

    @classmethod
    def setUpClass(cls):
        cls.file_path = "test_file.json"
        cls.file_path_backup = FileStorage._FileStorage__file_path

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

        FileStorage._FileStorage__file_path = cls.file_path_backup

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

    def test_get_constructor(self):
        """Test the 'get_constructor' method of FileStorage."""
        from models.base_model import BaseModel

        self.assertIs(self.fs.get_constructor("BaseModel"), BaseModel)
        self.assertIsNone(self.fs.get_constructor("FakeModel"))

    def test_all(self):
        """Test 'all' method of FileStorage class."""
        self.assertIs(self.fs.all(), FileStorage._FileStorage__objects)

    def test_new(self):
        """Test 'new' method of FileStorage."""
        from models.base_model import BaseModel

        objects = FileStorage._FileStorage__objects
        objects_copy = dict(objects)

        # create new object
        bm = BaseModel()
        bm_key = f"{bm.__class__.__name__}.{bm.id}"

        # check that the new object is now in __objects
        self.assertTrue(bm_key not in objects_copy)
        self.assertTrue(bm_key in objects)
        self.assertEqual(objects.get(bm_key), bm)

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

        # saving should create a new file
        self.fs.save()

        # check that file_path exists
        self.assertTrue(os.path.exists(file_path))

    def test_reload(self):
        """Test 'reload' method of FileStorage class."""
        from models.base_model import BaseModel

        objects = FileStorage._FileStorage__objects

        # create some BaseModel objects and save them to storage
        for i in range(2):
            BaseModel()

        self.fs.save()

        # clear the objects in memory
        objects_copy = dict(objects)
        objects.clear()
        self.assertTrue(len(objects) == 0)
        self.assertTrue(len(objects_copy) > 0)

        # reload objects from storage
        self.fs.reload()

        # check that the reload is successful
        for obj_key, obj in objects_copy.items():
            self.assertEqual(obj.to_dict(), objects[obj_key].to_dict())
