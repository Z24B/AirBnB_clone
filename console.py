#!/usr/bin/python3
"""Base Command Interpreter"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
import inspect


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if args and args[0] not in globals():
            print("** class doesn't exist **")
            return
        all_objects = models.storage.all()
        if args:
            class_name = args[0]
            print([
                str(value) for key, value in all_objects.items()
                if key.startswith(class_name)])
        else:
            print([str(value) for value in all_objects.values()])

    def default(self, arg):
        """Handles dynamic command <class name>.all()|<class name>.count()"""
        args = arg.split(".")
        if len(args) != 2:
            print("** invalid command **")
            return
        class_name, command = args
        if not hasattr(models, class_name):
            print("** class doesn't exist **")
            return
        cls = getattr(models, class_name)
        if not inspect.isclass(cls) or not issubclass(cls, BaseModel):
            print("** class doesn't exist **")
            return
        if command == "all()":
            print([str(value) for value in cls.all().values()])
        elif command == "count()":
            print(len(cls.all().values()))
        elif command.startswith("show(") and command.endswith(")"):
            obj_id = command[command.index("(") + 1:command.index(")")]
            key = "{}.{}".format(class_name, obj_id)
            all_objects = models.storage.all()
            if key not in all_objects:
                print("** no instance found **")
                return
            print(all_objects[key])
        elif command.startswith("destroy(") and command.endswith(")"):
            obj_id = command[command.index("(") + 1:command.index(")")]
            key = "{}.{}".format(class_name, obj_id)
            all_objects = models.storage.all()
            if key not in all_objects:
                print("** no instance found **")
                return
            del all_objects[key]
            models.storage.save()
        elif command.startswith("update(") and command.endswith(")"):
            args = command[command.index(
                "(") + 1:command.index(")")].split(", ")
            if len(args) != 2:
                print("** invalid update command **")
                return
            obj_id = args[0].strip('"')
            key = "{}.{}".format(class_name, obj_id)
            all_objects = models.storage.all()
            if key not in all_objects:
                print("** no instance found **")
                return
            try:
                update_dict = eval(args[1])
            except Exception:
                print("** invalid dictionary format **")
                return
            for k, v in update_dict.items():
                setattr(all_objects[key], k, v)
            all_objects[key].save()
        else:
            print("** invalid command **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
