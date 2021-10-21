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

    def test_args(self):
        b1 = Base(id=10)
        b2 = Base(id=100)
        self.assertIsNotNone(b1.id, b2.id)


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)


if __name__ == "__main__":
    unittest.main()
