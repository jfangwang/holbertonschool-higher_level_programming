#!/usr/bin/python3
"""unit test"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """test rectangle"""
    @classmethod
    def setUpClass(cls):
        """setup"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)

    def test_id(self):
        """test id - task 2"""
        Base._Base__nb_objects = 0
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_area(self):
        """test area - task 4"""
        Base._Base__nb_objects = 0
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r1.area(), 20)

    def test_display(self):
        """test display - task 5 and 7"""
        Base._Base__nb_objects = 0
        expected = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6)
            r1.display()
        self.assertEqual(fake_out.getvalue(), expected)
        expected = "\n\n  ##\n  ##\n  ##\n"
        """Task 7"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 3, 2, 2)
            r1.display()
        self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        """test str - task 6"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_attributes(self):
        """test get and set - task 3"""
        """width"""
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("test", 1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(1.1, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-1, 1)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, "test")
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, 1.1)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 1, -1, 1)

    def test_update(self):
        """test update 8 and 9"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """to dictionary - task 13"""
        Base._Base__nb_objects = 0
        rdict1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, rdict1)
        self.assertIs(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertNotEqual(r1, r2)
