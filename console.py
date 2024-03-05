#!/usr/bin/python3
"""Command interpreter program"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """No actions, empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
