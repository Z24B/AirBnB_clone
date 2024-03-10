#!/usr/bin/python3
"""Base Command Interpreter"""

import cmd
import inspect
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        from models import storage
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        from models import storage
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        from models import storage
        args = shlex.split(arg)
        if not args:
            print([str(value) for value in storage.all().values()])
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        print([
            str(value)
            for key, value in storage.all().items()
            if key.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        from models import storage
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.__all__:
            print("** class doesn't exist **")
            return
        cls = getattr(models, class_name)
        if not issubclass(cls, BaseModel):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        try:
            update_dict = eval(update_dict_str)
        except Exception:
            print("** invalid dictionary **")
            return
        if not isinstance(update_dict, dict):
            print("** invalid dictionary **")
            return
        for k, v in update_dict.items():
            setattr(all_objects[key], k, v)
        all_objects[key].save()

    def default(self, arg):
        """Handles dynamic commands"""
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
            args =
            command[command.index("(") + 1:command.index(")")].split(",")
            if len(args) < 3:
                print("** attribute name or value missing **")
                return
            obj_id = args[0].strip('"')
            key = "{}.{}".format(class_name, obj_id)
            all_objects = models.storage.all()
            if key not in all_objects:
                print("** no instance found **")
                return
            attr_name = args[1].strip('"')
            attr_value = args[2].strip('"')
            try:
                attr_value = eval(attr_value)
            except Exception:
                pass
            setattr(all_objects[key], attr_name, attr_value)
            all_objects[key].save()
        else:
            print("** invalid command **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
