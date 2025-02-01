from .vector import *
from useful_utility.exceptions import ArgumentException

import unittest

class test_vectors(unittest.TestCase):
    def test_vector_length(self):
        v: Vector = Vector(3, 4)
        self.assertEqual(v.length(), 5)
        coords_v: list = [1] * 25
        length_v: float = rnd(25 ** (1/25))
        v: Vector = Vector(*coords_v)
        self.assertEqual(v.length(), length_v)
        v: Vector = Vector(0)
        self.assertEqual(v.length(), 0)
        v: Vector = Vector(-1)
        self.assertEqual(v.length(), 1)

    def test_vector_init(self):
        Vector(5, 5, 5, 5)
        with self.assertRaises(ArgumentException):
            Vector()
            Vector(5, 5, None)
            Vector(5, 5, "5")

    def test_vector_add(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(2, 2)
        self.assertEqual(v1 + v2, Vector(3, 3))

if __name__ == "__main__":
    unittest.main()
