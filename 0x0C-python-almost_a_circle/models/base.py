#!/usr/bin/python3
# base.py
# Juan Duque <3428@holbertonschool.com>
"""Import the libraries
    unittest"""
import unittest


class Base:

    __nb_objects = 0

    @classmethod
    def __init__(self, id=None):

        if id is not None:
            self.id = id
