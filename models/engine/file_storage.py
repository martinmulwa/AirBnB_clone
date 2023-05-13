#!/usr/bin/python3
"""FileStorage module."""


class FileStorage:
    """Implements a simple file storage."""

    __file_path = ""
    __objects = {}

    def all(self):
        """Return dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add obj to __objects with key <obj class name>.id."""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj
