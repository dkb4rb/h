#!/usr/bin/python3
# 11-square.py
# Juan Duque <3428@holbertonschool.com>
"""
Import module what contain new Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

"""Define the new class"""


class Square(Rectangle):
    """ Reference to Square class inheritance"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
