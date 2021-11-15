#!/usr/bin/python3
"""
This file is the entry point of
the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity

class_names = ["BaseModel", "User", "State", "City",
               "Review", "Place", "Amenity"]


class HBNBCommand(cmd.Cmd):
    """
    This program contains the entry point
    of the command interpreter
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Command that creates a new instance of a class,
        saves it to a JSON file and prints the id.
        Usage:
              create <class_name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in class_names:
            print("** class doesn't exist **")
        else:
            class_obj = eval(f"{arg}()")
            class_obj.save()
            print(class_obj.id)

    def do_show(self, arg):
        """
        Command that prints the string representation of
        an instance based on the class name and id.
        Usage:
              show <class_name> <object_id>
        """
        list_arg = arg.split()

        try:
            name = list_arg[0]
            id_in_arg = list_arg[1]
        except Exception:
            pass

        if not arg:
            print("** class name missing **")
        elif name not in class_names:
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            dict_obj = models.storage.all()
            found_id = False
            for value in dict_obj.values():
                obj_id = value.id
                if obj_id == id_in_arg:
                    found_id = True
                    print(value)
            if found_id is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Command that deletes an instance based on the class name
        and id. It saves the change into the JSON file.
        Usage:
              destroy <class_name> <object_id>
        """
        list_arg = arg.split()

        try:
            name = list_arg[0]
            id_in_arg = list_arg[1]
        except Exception:
            pass

        if not arg:
            print("** class name missing **")
        elif name not in class_names:
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            dict_obj = models.storage.all()
            found_id = False
            copy_dict_obj = dict_obj.copy()
            for key, value in copy_dict_obj.items():
                obj_id = value.id
                if obj_id == id_in_arg:
                    found_id = True
                    dict_obj.pop(key)
                    models.storage.save()
            if found_id is False:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Command that prints all string representation of
        all instances based or not on the class name
        Usage:
              - To show all instances of all classes: all
              - To show all instances of a specific class: all <class_name>
        """

        dic_model = models.storage.all()
        list_all = []

        if not arg:
            for value in dic_model.values():
                str_obj = value.__str__()
                list_all.append(str_obj)
            print(list_all)
        elif arg in class_names:
            for value in dic_model.values():
                if value.__class__.__name__ == arg:
                    str_obj = value.__str__()
                    list_all.append(str_obj)
            print(list_all)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute.
        (Only one attribute at the time).
        It saves the change into the JSON file.
        Usage:
              update <class name> <id> <attribute name> "<attribute value>"
        """
        list_arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif list_arg[0] not in class_names:
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        elif list_arg[1]:
            dict_obj = models.storage.all()
            found_id = False
            for value in dict_obj.values():
                obj_id = value.id
                if obj_id == list_arg[1]:
                    found_id = True
                    if len(list_arg) < 3:
                        print("** attribute name missing **")
                        break
                    elif len(list_arg) < 4:
                        print("** value missing **")
                        break

                    id_to_update = list_arg[1]
                    name_attribute = list_arg[2]
                    val_att = list_arg[3]

                    if val_att.startswith('"'):
                        v = list_arg[3:]
                        if v[0].endswith('"'):
                            val_att = v[0].strip('"')
                        else:
                            for arg in v:
                                if arg.endswith('"'):
                                    val_att = " ".join(v[0:(v.index(arg) + 1)])
                                    val_att = val_att.strip('"')
                                    break
                    else:
                        if "." in val_att:
                            val_att = float(val_att)
                        else:
                            val_att = int(val_att)

                    setattr(value, name_attribute, val_att)
                    models.storage.save()

            if found_id is False:
                print("** no instance found **")

    def do_quit(self, arg):
        """
        Command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command to exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
