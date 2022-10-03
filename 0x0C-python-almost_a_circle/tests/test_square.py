#!/usr/bin/python3
"""Unittest for Square module"""

from models.square import Square
from unittest import TestCase


class TestSquare(TestCase):
    def test_size_get(self):
        """ Test's for size method """

        s1 = Square(10, 5, 3, 1)
        self.assertEqual(s1.size, 10)

    def test_size_set(self):
        """ Test's for size method """

        s1 = Square(10, 5, 3, 1)
        s1.size = 100

        self.assertEqual(s1.size, 100)

    def test_y_not_int(self):
        """ Test's for y method """

        r1 = Square(3, 4, 0, 0)

        with self.assertRaises(TypeError):
            r1.y = "51"

    def test_update(self):
        """ Test's for update method """

        s1 = Square(10, 5, 3, 1)
        s1.update(11, 6, 4, 2)

        self.assertEqual(s1.id, 11)

        self.assertEqual(s1.size, 6)

        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 2)

    def test_to_dictionary(self):
        """ Test's for to_dictionary method """

        test_dict = {'id': 1, 'size': 4, 'x': 2, 'y': 1}
        r1 = Square(4, 2, 1, 1)

        self.assertEqual(test_dict, r1.to_dictionary())
