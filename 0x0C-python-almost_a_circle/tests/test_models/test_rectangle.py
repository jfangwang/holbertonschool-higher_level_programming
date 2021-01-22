#!/usr/bin/python3
"""unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """test rectangle"""
    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)

    def test_id(self):
        """test id - task 2"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_area(self):
        """test area - task 4"""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r1.area(), 20)

    def test_display(self):
        """test display - task 5 and 7"""
        pass

    def test_str(self):
        """test str - task 6"""
        pass

    def test_attributes(self):
        """test get and set - task 3"""
        """width"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("test", 1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(1.1, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-1, 1)
        """height"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, "test")
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, 1.1)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, -1)
        """y"""
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(1, 1, 1, -1)
        """x"""
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 1, -1, 1)

    @classmethod
    def tearDownClass(cls):
        """del instances"""
        pass
