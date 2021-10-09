#!/usr/bin/python3

from typing import Type


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
