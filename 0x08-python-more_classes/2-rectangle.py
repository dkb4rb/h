#!/usr/bin/python3
# File: 1-rectangle.py
# Juan Duque <3428@holbertonschool.com>


class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return((self.__width * 2) + (self.height * 2))
