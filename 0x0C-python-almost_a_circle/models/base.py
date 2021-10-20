#!/usr/bin/python3
# base.py
# Juan Duque <3428@holbertonschool.com>
"""Import the libraries"""
import json
import csv
import turtle


class Base:
    """ This is the reference of the Base class"""
    __nb_objects = 0

    """ Instance new Base 
    
        Args: 
            Id (int): Identity of the new Base"""

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
