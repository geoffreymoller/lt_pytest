from unittest import TestCase

from math_is_fun import *


class Test(TestCase):

    def test_add(self):
        self.assertEqual(add(1, 3), 4, msg='equal')

    def test_subtract(self):
        self.assertEqual(subtract(3, 1), 2, msg='equal')

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6, msg='equal')

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3, msg='equal')

    def test_exponent(self):
        self.assertEqual(exponent(6, 2), 36, msg='equal')