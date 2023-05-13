#!/usr/bin/python3
"""FileStorage module."""

import json


class FileStorage:
    """Implements a simple file storage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add obj to __objects with key <obj class name>.id."""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        objects_serialized = {}

        # ensure every object in __objects can be serialized
        for obj_key, obj in self.__objects.items():
            try:
                objects_serialized[obj_key] = obj.to_dict()
            except Exception:
                objects_serialized[obj_key] = obj.__dict__

        # write objects_serialized to file_path
        try:
            with open(self.__file_path, "w") as f_write:
                json.dump(objects_serialized, f_write)
        except Exception:
            raise Exception(f"Error: Could not open {self.__file_path}")
