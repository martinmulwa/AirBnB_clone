#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """

    prompt = "(hbnb) "
    classes = {}

    def do_quit(self, arg):
        """
        Exit program on quit command
        """
        return True

    def do_EOF(self, arg):
        """
        Exit program on EOF command
        """
        print()
        return True

    def emptyline(self):
        """
        Execute nothing when empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if len(arg) > 0 and arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(arg) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg[0], arg[1])) not in storage.all():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** no instance found **")
        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
