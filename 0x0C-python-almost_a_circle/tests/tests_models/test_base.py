#!/usr/bin/python3
# test_base.py
# Juan Duque <3428@holbertonschool.com>
""" Impor the libraries and modules to testing 

    Unittest Modules:
    """
import os
import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_not_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)


if __name__ == "__main__":
    unittest.main()
