#!/usr/bin/python3
"""FileStorage module."""

import json
from models.base_model import BaseModel


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
            raise Exception(f"Error: Could not write to {self.__file_path}")

    def reload(self):
        """Deserializes JSON file to __objects."""
        try:
            # remove all objects currently in memory
            self.__objects.clear()

            # read content of file_path
            try:
                with open(self.__file_path, "r") as f_read:
                    objects_loaded = json.load(f_read)
            except Exception:
                raise Exception(f"Error: Could not read {self.__file_path}")

            # deserialize the objects in objects_loaded
            for obj_key, obj_dict in objects_loaded.items():
                class_name = globals()[obj_dict["__class__"]]
                obj = class_name(**obj_dict)
                self.__objects[obj_key] = obj

        except FileNotFoundError:
            pass
