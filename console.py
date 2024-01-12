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


