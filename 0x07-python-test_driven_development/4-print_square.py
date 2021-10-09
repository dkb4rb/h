#!/usr/bin/python3
# 4-print_square.py
# Juan Duque <3428@holbertonschool.com>

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
