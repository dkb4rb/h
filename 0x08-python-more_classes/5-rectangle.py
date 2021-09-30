#!/usr/bin/python3
# 3-rectangle.py
# Juan Duque <3428@holbertonschool.com>

"""Define Class Rectangle"""


from typing import Type


class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Declare delet method"""

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Declaration of the area method"""

    def area(self):
        return self.__width * self.__height

    """Declaration of the perimeter method"""

    def perimeter(self):
        if self.__height != 0 or self.__width != 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
