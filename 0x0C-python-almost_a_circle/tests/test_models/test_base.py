#!/usr/bin/python3
"""unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_base(unittest.TestCase):
    """test base"""

    @classmethod
    def setUpClass(cls):
        """set up instances"""
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(12)
        cls.b5 = Base()

    def test_id(self):
        """test id"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
