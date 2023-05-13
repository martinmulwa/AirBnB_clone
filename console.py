#!/usr/bin/python3
"""
Module cmd
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """

    def do_quit(self, arg):
        """
        Exit program
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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
