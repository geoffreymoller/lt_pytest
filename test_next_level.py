from unittest import TestCase

from next_level_multiply_and_split import *


class Test(TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6, msg='equal')

    def test_split(self):
        self.assertEqual(split("one two three"), ["one","two","three"], msg='equal')
