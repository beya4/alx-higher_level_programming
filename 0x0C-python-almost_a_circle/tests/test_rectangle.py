#!/usr/bin/python3
""" Test's for rectangle class """

from models.rectangle import Rectangle
from unittest import TestCase
from io import StringIO
import sys


class TestRectangle(TestCase):
    """ Test's for base class methods """

    def test___init__(self):
        """ Test's for init method """
        r2 = Rectangle(3, 4, 6, 1, 5)

        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertEqual(r2.id, 5)

        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.width, 3)

        self.assertEqual(r2.x, 6)
        self.assertEqual(r2.y, 1)

    def test_height(self):
        """ Test's for height method """

        r1 = Rectangle(3, 4, 0, 0)
        r1.height = 5191

        self.assertTrue(Rectangle.height.__doc__)
        self.assertEqual(r1.height, 5191)

    def test_height_not_int(self):
        """ Test's for y method """

        r1 = Rectangle(3, 4, 0, 0)

        with self.assertRaises(TypeError):
            r1.height = "51"

    def test_width(self):
        """ Test's for width method """

        r1 = Rectangle(3, 4, 0, 0)
        r1.width = 5191

        self.assertTrue(Rectangle.width.__doc__)
        self.assertEqual(r1.width, 5191)

    def test_width_not_int(self):
        """ Test's for y method """

        r1 = Rectangle(3, 4, 0, 0)

        with self.assertRaises(TypeError):
            r1.width = "51"

    def test_x(self):
        """ Test's for x method """

        r1 = Rectangle(3, 4, 0, 0)
        r1.x = 5191

        self.assertTrue(Rectangle.x.__doc__)
        self.assertEqual(r1.x, 5191)

    def test_x_not_int(self):
        """ Test's for y method """

        r1 = Rectangle(3, 4, 0, 0)

        with self.assertRaises(TypeError):
            r1.x = "51"

    def test_y(self):
        """ Test's for y method """

        r1 = Rectangle(3, 4, 0, 0)
        r1.y = 5191

        self.assertTrue(Rectangle.y.__doc__)
        self.assertEqual(r1.y, 5191)

    def test_y_not_int(self):
        """ Test's for y method """

        r1 = Rectangle(3, 4, 0, 0)

        with self.assertRaises(TypeError):
            r1.y = "51"

    def test_area(self):
        """ Test's for area method """

        r1 = Rectangle(3, 4, 0, 0)

        self.assertEqual(r1.area(), 12)

    def test_display(self):
        """ Test's for display method """

        local_stdout = StringIO()
        sys.stdout = local_stdout

        r1 = Rectangle(3, 2, 1, 2)
        r1.display()

        sys.stdout = sys.__stdout__
        value = local_stdout.getvalue()
        self.assertEqual("\n\n ###\n ###\n", value)

    def test_update(self):
        """ Test's for update method """

        r1 = Rectangle(3, 2, 1, 2)
        r1.update(5, 6, 7, 8, 9)

        self.assertEqual(r1.id, 5)

        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)

        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 9)

    def test_to_dictionary(self):
        """ Test's for to_dictionary method """

        test_dict = {'id': 5, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
        r1 = Rectangle(4, 3, 2, 1, 5)

        self.assertEqual(test_dict, r1.to_dictionary())
