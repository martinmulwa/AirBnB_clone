#!/usr/bin/python3
"""FileStorage module."""


class FileStorage:
    """Implements a simple file storage."""

    __file_path = ""
    __objects = {}

    def all(self):
        """Return dictionary of all stored objects."""
        return self.__objects
