#!/usr/bin/python3
# 1-write_file.py
# Juan Duque <3428@holbertonschool.com>

""" Define function to read new file"""


def write_file(filename="", text=""):
    """"Writing in to fle with statement
        Return - 29

    """
    with open(filename, 'w') as file:
        file.write(text)
    return(29)
