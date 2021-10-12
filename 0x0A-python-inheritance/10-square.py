#!/usr/bin/python3
# 10-square.py
# Juan Duque <3428@holbertonschool.com>
"""
Import the modul what contain the new rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Rectangle subclass Square."""


class Square(Rectangle):
    """ A square """

    def __init__(self, size):
        """Init a square
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
