#!/usr/bin/python3

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")