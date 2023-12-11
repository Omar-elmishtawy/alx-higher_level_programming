#!/usr/bin/python3
"""Defines unittests for base.py.
"""
import unittest
from models.base import Base


class TestBase_instansiation(unittest.TestCase):
    """unit test for testing Base instansiation"""

    def setUp(self):
        "setup for start pf every test"
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_change_id(self):
        b1 = Base()
        b2 = Base(12)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
    if __name__ == "__main__":
        unittest.main()
