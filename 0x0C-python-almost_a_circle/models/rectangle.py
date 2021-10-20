#!/usr/bin/python3
# rectangle.py
# Juan Duque <3428@holbertonschool.com>
"""Import the libraries"""
import json
import csv
import turtle

Base = __import__('base').Base

""" Define new class rectangle inherits of the class
    Base"""


class rectangle(Base):
    """ This is reference to rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id


if __name__ == "__main__":

    list = ["", ""]

    rec = rectangle(20, 30, 40, 50, 2312)
    rec2 = rectangle(10, 20, 30, 40, 23)

    list[0] = rec
    list[1] = rec2

    print(list[0].__dict__)
    print(list[1].__class__)
