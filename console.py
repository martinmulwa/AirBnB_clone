#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter
    """

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place
    }

    def do_quit(self, args):
        """Exit program on quit command
        """
        return True

    def do_EOF(self, args):
        """Exit program on EOF command
        """
        print()
        return True

    def emptyline(self):
        """Execute nothing when empty line is entered
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        """
        args_list = shlex.split(args)

        # check if no argument is provided
        if len(args_list) < 1:
            print("** class name missing **")
            return

        # check if too many arguments are provided
        if len(args_list) > 1:
            print("** too many arguments **")
            return

        # check if class name exists
        class_name = args_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # create new object using given class
        constructor = self.classes[class_name]
        instance = constructor()

        # print id of created object
        print(instance.id)

        # save to storage
        storage.save()

    def do_show(self, args):
        """Prints the string representation of an instance
        """

        args_list = shlex.split(args)

        # check if no argument is provided
        if len(args_list) < 1:
            print("** class name missing **")
            return

        # check if class name exists
        class_name = args_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # check if no argument is provided
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        # check if too many arguments are provided
        if len(args_list) > 2:
            print("** too many arguments provided **")
            return

        id = args_list[1]
        object_key = f"{class_name}.{id}"

        objects = storage.all()
        object = objects.get(object_key)

        # check if id is valid
        if object is None:
            print("** no instance found **")
            return

        # print string representation of the object
        print(object)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        args_list = shlex.split(args)

        # check if no argument is provided
        if len(args_list) < 1:
            print("** class name missing **")
            return

        # check if class name exists
        class_name = args_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # check if no argument is provided
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        # check if too many arguments are provided
        if len(args_list) > 2:
            print("** too many arguments provided **")
            return

        id = args_list[1]
        object_key = f"{class_name}.{id}"

        objects = storage.all()
        object = objects.get(object_key)

        # check if id is valid
        if object is None:
            print("** no instance found **")
            return

        del objects[object_key]

        # save to storage
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        """

        args_list = shlex.split(args)
        objects = storage.all()
        objects_str_list = []

        # if no arguments are provided
        if len(args_list) == 0:
            for object in objects.values():
                objects_str_list.append(str(object))
            print(objects_str_list)
            return

        # check if class name exists
        class_name = args_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # check if too many arguments are provided
        if len(args_list) > 1:
            print("** too many arguments provided **")
            return

        for object_key, object in objects.items():
            object_name = object_key.split('.')[0]
            if object_name == class_name:
                objects_str_list.append(str(object))

        # print list of string representations
        print(objects_str_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        """

        args_list = shlex.split(args)
        objects = storage.all()

        # check if no argument is provided
        if len(args_list) < 1:
            print("** class name missing **")
            return

        # check if class name exists
        class_name = args_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # check if no id argument is provided
        if len(args_list) < 2:
            print("** instance id missing **")
            return

        id = args_list[1]
        object_key = f"{class_name}.{id}"

        objects = storage.all()
        object = objects.get(object_key)
        object_class = self.classes[class_name]

        # check if id is valid
        if object is None:
            print("** no instance found **")
            return

        # check if no attribute_name argument is provided
        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args_list[2]

        # check if no attribute_value argument is provided
        if len(args_list) < 4:
            print("** value missing **")
            return

        attribute_value = args_list[3]

        # if attribute exists in the object, cast it to the correct type
        if hasattr(object_class, attribute_name):

            attribute_type = type(getattr(object_class, attribute_name))

            try:
                attribute_value = attribute_type(attribute_value)
            except Exception:
                raise Exception("Error: Casting failed")

        # set the value of attribute_name to attribute_value
        try:
            setattr(object, attribute_name, attribute_value)
        except Exception:
            raise Exception("Error: Update failed")

        # save to storage
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
