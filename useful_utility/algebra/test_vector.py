import unittest

from useful_utility.algebra.vector import *
from useful_utility.algebra.statics import rnd
from useful_utility.errors import ArgumentError, MathError

class TestVector(unittest.TestCase):
    def test_init(self):
        Vector(5, 5, 5, 5)
        with self.assertRaises(ArgumentError):
            Vector()
            Vector(5, 5, None)
            Vector(5, 5, "5")

    def test_length(self):
        v: Vector = Vector(2, 3, 4)
        self.assertEqual(v.length(), 5)
        coords_v: list = [1] * 25
        length_v: float = rnd(25 ** (1/2))
        v: Vector = Vector(25, *coords_v)
        self.assertEqual(v.length(), length_v)
        v: Vector = Vector(1, 0)
        self.assertEqual(v.length(), 0)
        v: Vector = Vector(1, -1)
        self.assertEqual(v.length(), 1)

    def test_add(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(2, 2)
        self.assertEqual(v1 + v2, Vector(3, 3))
        v1: Vector = Vector(2, 1, 1)
        v2: Vector = Vector(2, 1, 1)
        self.assertEqual(v1 + v2, Vector(2, 2, 2))
        v1: Vector = Vector(2, 0, -1)
        v2: Vector = Vector(2, 5, -3)
        self.assertEqual(v1 + v2, Vector(2, 5, -4))
        v1: Vector = Vector(2, 1, 1)
        v2: Vector = Vector(2, 1, 0)
        self.assertEqual(v1 + v2, Vector(2, 2, 1))
        with self.assertRaises(MathError):
            v1 + "5"

    def test_sub(self):
        v1: Vector = Vector(2, 1, 1)
        v2: Vector = Vector(2, 1, 1)
        self.assertEqual(v1 - v2, Vector(2, 0, 0))
        v1: Vector = Vector(2, 1, 0)
        v2: Vector = Vector(2, 1, 1)
        self.assertEqual(v1 - v2, Vector(2, 0, -1))
        v1: Vector = Vector(2, 1, 1)
        v2: Vector = Vector(2, 1, 1)
        self.assertEqual(v1 - v2, Vector(2, 0, 0))
        v1: Vector = Vector(2, 1, 1)
        v2: Vector = Vector(2, 1, 1)
        self.assertEqual(v1 - v2, Vector(2, 0, 0))
        with self.assertRaises(MathError):
            v1 - "5"

    def test_iadd(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 1)
        v1 += v2
        self.assertEqual(v1, Vector(2, 2))

    def test_isub(self):
        v1: Vector = Vector(1, 1, 1)
        v2: Vector = Vector(1, 1, 1)
        v1 -= v2
        self.assertEqual(v1, Vector(1, 0, 0))

    def test_mul(self):
        v1: Vector = Vector(2, 1, 1)
        v2: Vector = Vector(2, 2, 1)
        self.assertEqual(v1 * v2, 3)
        v1: Vector = Vector(2, 2, 5)
        sc: float = 5
        v1.__mul__(sc)
        self.assertEqual(v1 * sc, Vector(2, 10, 25))
        with self.assertRaises(MathError):
            v1 * "5"

    def test_imul(self):
        v1: Vector = Vector(2, 1, 1)
        sc: float = 5
        v1 *= sc
        self.assertEqual(v1, Vector(2, 5, 5))
        with self.assertRaises(MathError):
            v1 *= Vector(2, 1, 1)
            v1 *= "5"

    def test_div(self):
        v1: Vector = Vector(1, 1)
        sc: float = 0
        with self.assertRaises(MathError):
            v1 / 0
        sc: float = 2
        self.assertEqual(v1 / sc, Vector(2, .5, .5))
        with self.assertRaises(MathError):
            v1 / "5"

    def test_idiv(self):
        v1: Vector = Vector(2, 1, 1)
        v1 /= 5
        self.assertEqual(v1, Vector(2, .2, .2))
        with self.assertRaises(MathError):
            v1 /= 0
        with self.assertRaises(MathError):
            v1 /= "5"

if __name__ == "__main__":
    unittest.main()
