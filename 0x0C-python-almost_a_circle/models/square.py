#!/usr/bin/python3
# square.py
# Juan Duque <3428@holbertonschool.com>
""" Import the class for inheritance"""
from models.rectangle import Rectangle
from models.base import Base

""" Define new class Square inherits to Rectangle"""


class Square(Rectangle):
    """ This is reference to Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
