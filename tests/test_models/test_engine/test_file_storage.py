#!/usr/bin/python3
"""Test FileStorage module."""

from models.engine.file_storage import FileStorage
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
        """Test all method of FileStorage objects."""
        fs = FileStorage()

        self.assertIs(fs.all(), FileStorage._FileStorage__objects)
