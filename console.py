#!/usr/bin/python3
"""contains the entry point of the command interpreter"""


import cmd
import re
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    """defines the HBNB """

    prompt = "(hbnb)"

    def EOF(self, line):
        """end of the file"""

        print()
        return True

    def quit(self, line):
        """exit the porgam"""

        return True

    def Enter(self, line):
        """handle the enter"""

        pass

    def create(self, line):
        """ Creates a new instance of BaseModel"""

        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)
