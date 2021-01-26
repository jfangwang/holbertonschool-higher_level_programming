#!/usr/bin/python3
"""unit test"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):
    """test square unit test"""
    def test_square(self):
        """test square - task 10"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        expected = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
        self.assertEqual(fake_out.getvalue(), expected)
        s2 = Square(2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        expected = "  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s2.display()
        self.assertEqual(fake_out.getvalue(), expected)
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        expected = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s3.display()
        self.assertEqual(fake_out.getvalue(), expected)

    def test_size(self):
        """square size - task 11"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "9"
            str(s1)
    def test_square_update(self):
        """square update - task 12"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """to dictionary - task 14"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        sdict1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary, sdict1)
        self.assertIs(type(s1_dictionary), dict)
        
        s2 = Rectangle(1, 1)
        s2.update(**s1_dictionary)
        self.assertNotEqual(s1, s2)

