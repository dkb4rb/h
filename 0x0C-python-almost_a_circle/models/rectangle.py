#!/usr/bin/python3
# rectangle.py
# Juan Duque <3428@holbertonschool.com>
"""Import the libraries"""
import json
import csv
import turtle
from models.base import Base

""" Define new class rectangle inherits of the class
    Base"""


class Rectangle(Base):
    """ This is reference to rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)


if __name__ == "__main__":

    list = ["", ""]

    rec = Rectangle(20, 30, 40, 50, 2312)
    rec2 = Rectangle(10, 20, 30, 40, 23)

    list[0] = rec
    list[1] = rec2

    print(list[0].__dict__)
    print(list[1].__class__)
