import unittest

from .vector import *
from useful_utility.exceptions import ArgumentException

class TestVector(unittest.TestCase):
    def test_init(self):
        Vector(5, 5, 5, 5)
        with self.assertRaises(ArgumentException):
            Vector()
            Vector(5, 5, None)
            Vector(5, 5, "5")

    def test_length(self):
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

    def test_add(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(2, 2)
        self.assertEqual(v1 + v2, Vector(3, 3))
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 1, 1)
        self.assertEqual(v1 + v2, Vector(2, 2, 1))
        v1: Vector = Vector(1, 0, -1)
        v2: Vector = Vector(0, 5, -3)
        self.assertEqual(v1 + v2, Vector(1, 5, -4))
        v1: Vector = Vector(1, 1, 1)
        v2: Vector = Vector(1, 1)
        self.assertEqual(v1 + v2, Vector(2, 2, 1))
        with self.assertRaises(TypeError):
            v1 + "5"

    def test_sub(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 1)
        self.assertEqual(v1 - v2, Vector(0, 0))
        v1: Vector = Vector(1, 0)
        v2: Vector = Vector(1, 1)
        self.assertEqual(v1 - v2, Vector(0, -1))
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 1)
        self.assertEqual(v1 - v2, Vector(0, 0))
        v1: Vector = Vector(1, 1, 1)
        v2: Vector = Vector(1, 1)
        self.assertEqual(v1 - v2, Vector(0, 0, 1))
        with self.assertRaises(TypeError):
            v1 - "5"

    def test_iadd(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 1)
        v1 += v2
        self.assertEqual(v1, Vector(2, 2))

    def test_isub(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 1)
        v1 -= v2
        self.assertEqual(v1, Vector(0, 0))

    def test_mul(self):
        v1: Vector = Vector(1, 1)
        v2: Vector = Vector(1, 2)
        self.assertEqual(v1 * v2, 3)
        v1: Vector = Vector(2, 5)
        sc: float = 5
        self.assertEqual(v1 * sc, Vector(10, 25))
        with self.assertRaises(TypeError):
            v1 * "5"

    def test_imul(self):
        v1: Vector = Vector(1, 1)
        sc: float = 5
        v1 *= sc
        self.assertEqual(v1, Vector(5, 5))
        with self.assertRaises(TypeError):
            v1 *= Vector(1, 1)
            v1 *= "5"

    def test_div(self):
        v1: Vector = Vector(1, 1)
        sc: float = 0
        with self.assertRaises(ZeroDivisionError):
            v1 / 0
        sc: float = 2
        self.assertEqual(v1 / sc, Vector(.5, .5))
        with self.assertRaises(TypeError):
            v1 / "5"

    def test_idiv(self):
        v1: Vector = Vector(1, 1)
        v1 /= 5
        self.assertEqual(v1, Vector(.2, .2))
        with self.assertRaises(ZeroDivisionError):
            v1 /= 0
        with self.assertRaises(TypeError):
            v1 /= "5"


class TestVector2D(unittest.TestCase):
    def test_init(self):
        Vector2D(1, 1)
        with self.assertRaises(ArgumentException):
            Vector2D(1, None)
            Vector2D(1, "0")
            Vector2D("0", 0)

    def test_length(self):
        v1: Vector2D = Vector2D(3, 4)
        self.assertEqual(v1.length(), 5)
        v1: Vector2D = Vector2D(3, -4)
        self.assertEqual(v1.length(), 5)
        v1: Vector2D = Vector2D(-3, 4)
        self.assertEqual(v1.length(), 5)
        v1: Vector2D = Vector2D(-3, -4)
        self.assertEqual(v1.length(), 5)

    def test_complex(self):
        v1: Vector2D = Vector2D(1, 1)
        self.assertEqual(v1.get_complex(), complex(1, 1))

    def test_from_vector(self):
        v1: Vector2D = Vector2D.from_vector(Vector(1, 1))
        self.assertEqual(v1, Vector2D(1, 1))
        v1: Vector2D = Vector2D.from_vector(Vector(1))
        self.assertEqual(v1, Vector2D(1, 0))
        v1: Vector2D = Vector2D.from_vector(Vector(1, 1, 1))
        self.assertEqual(v1, Vector2D(1, 1))
        v1: Vector2D = Vector2D.from_vector(Vector3D(1, 1, 1))
        self.assertEqual(v1, Vector2D(1, 1))

    def test_angle(self):
        v1: Vector2D = Vector2D(1, 0)
        v2: Vector2D = Vector2D(0, 1)
        self.assertEqual(v1.angle(v2), math.pi/2)

    def test_add(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(v1 + c, Vector(2, 2))
        c: complex = complex(0, 0)
        self.assertEqual(v1 + c, Vector(1, 1))

    def test_radd(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(c + v1, Vector(2, 2))
        c: complex = complex(0, 0)
        self.assertEqual(c + v1, Vector(1, 1))

    def test_sub(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(v1 - c, Vector(0, 0))
        c: complex = complex(0, 0)
        self.assertEqual(v1 - c, Vector(1, 1))

    def test_rsub(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(c - v1, Vector(0, 0))
        c: complex = complex(0, 0)
        self.assertEqual(c - v1, Vector(1, 1))

    def test_mul(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(v1 * c, Vector(0, 2))
        c: complex = complex(0, 0)
        self.assertEqual(v1 * c, Vector(0, 0))

    def test_rmul(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(c * v1, Vector(0, 2))
        c: complex = complex(0, 0)
        self.assertEqual(c * v1, Vector(0, 0))

    def test_div(self):
        v1: Vector2D = Vector2D(1, 1)
        c: complex = complex(1, 1)
        self.assertEqual(v1 / c, Vector(1, 0))
        c: complex = complex(0, 0)
        with self.assertRaises(ZeroDivisionError):
            v1 / c

class TestVector3D(unittest.TestCase):
    def test_init(self):
        Vector3D(1, 1, 1)
        with self.assertRaises(ArgumentException):
            Vector3D(1, None, 1)
            Vector3D("5")
            Vector3D(None)

    def test_from_vector(self):
        v1: Vector3D = Vector3D.from_vector(Vector(1, 1, 1))
        self.assertEqual(v1, Vector3D(1, 1, 1))
        v1: Vector3D = Vector3D.from_vector(Vector(1, 1, 1, 1))
        self.assertEqual(v1, Vector3D(1, 1, 1))
        v1: Vector3D = Vector3D.from_vector(Vector(1, 1))
        self.assertEqual(v1, Vector3D(1, 1))
        v1: Vector3D = Vector3D.from_vector(Vector2D(1, 1))
        self.assertEqual(v1, Vector3D(1, 1))

if __name__ == "__main__":
    unittest.main()
