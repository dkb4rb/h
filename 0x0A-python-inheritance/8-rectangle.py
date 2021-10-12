#!/usr/bin/python3
# 8-rectangle.py
# Juan Duque <3428@holbertonschool.com>
"""
Import the class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Define the new class whit name of the Rectangle
    and inherits of the BaseGeometry"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
