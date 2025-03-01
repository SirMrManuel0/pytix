import unittest
import numpy as np

from useful_utility.algebra import Matrix
from useful_utility.errors import *

class TestMatrix(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Matrix([[1, 2], [1, 2]], 2, 2),
                         Matrix([[1, 2], [1, 2]], 2, 2))
        self.assertEqual(Matrix([[1, 2], [1, 2]], 2, 2),
                         np.array([[1, 2], [1, 2]]))

        with self.assertRaises(ArgumentError):
            Matrix("a")
            Matrix(rows="a")
            Matrix(data="a")
            Matrix(-1)
            Matrix(rows=-1)
            Matrix(0)
            Matrix(rows=0)
            Matrix(data=["a"])

    def test_set_components(self):
        m: Matrix = Matrix([[1, 2], [1, 2]], 2, 2)
        m.set_components([[1, 1], [1, 2]])
        self.assertEqual(m, np.array([[1, 1], [1, 2]]))
        n: np.ndarray = np.array([[1], [0]])
        m.set_components(n)
        self.assertEqual(m, n)
        self.assertEqual(m.get_dimension(), (2, 1))
        m.set_components([1, 1])
        self.assertEqual(m, np.array([[1], [1]]))
        m.set_components([[np.float64(5.01), np.float64(5.01)], [np.float64(5.01), np.float64(5.01)]])
        self.assertEqual(m, np.array([[np.float64(5.01), np.float64(5.01)], [np.float64(5.01), np.float64(5.01)]]))

        with self.assertRaises(ArgumentError):
            m.set_components((1, 1))
            m.set_components(1)
            m.set_components(["a", 2])

    def test_copy(self):
        m: Matrix = Matrix([1, 2])
        v: Matrix = m.copy()
        b: bool = hex(id(v)) == hex(id(m))
        self.assertFalse(b)

    def test_create_identity_matrix(self):
        m: Matrix = Matrix.create_identity_matrix()
        self.assertEqual(m, np.array([[1, 0], [0, 1]]))
        with self.assertRaises(ArgumentError):
            Matrix.create_identity_matrix(1.06)
            Matrix.create_identity_matrix("1.061.06")
            Matrix.create_identity_matrix([1])

    def test_add(self):
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [1, 1]])
        self.assertEqual(m1 + m2, np.array([[2, 2], [2, 2]]))
        m1: Matrix = Matrix([[1, -1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [-1, 1]])
        self.assertEqual(m1 + m2, np.array([[2, 0], [0, 2]]))
        m1: Matrix = Matrix([[1, 3, 2], [9, 1, 2]])
        m2: Matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        self.assertEqual(m1 + m2, np.array([[2, 4, 3], [10, 2, 3]]))

        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m2: Matrix = Matrix([[1, 1], [1, 1]])
            m3: Matrix = m1 + m2
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m3: Matrix = m1 + 7

    def test_iadd(self):
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [1, 1]])
        m1 += m2
        self.assertEqual(m1, np.array([[2, 2], [2, 2]]))
        m1: Matrix = Matrix([[1, -1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [-1, 1]])
        m1 += m2
        self.assertEqual(m1, np.array([[2, 0], [0, 2]]))
        m1: Matrix = Matrix([[1, 3, 2], [9, 1, 2]])
        m2: Matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        m1 += m2
        self.assertEqual(m1, np.array([[2, 4, 3], [10, 2, 3]]))

        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m2: Matrix = Matrix([[1, 1], [1, 1]])
            m1 += m2
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m1 += 7

    def test_sub(self):
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [1, 1]])
        self.assertEqual(m1 - m2, np.array([[0, 0], [0, 0]]))
        m1: Matrix = Matrix([[1, -1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [-1, 1]])
        self.assertEqual(m1 - m2, np.array([[0, -2], [2, 0]]))
        m1: Matrix = Matrix([[1, 3, 2], [9, 1, 2]])
        m2: Matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        self.assertEqual(m1 - m2, np.array([[0, 2, 1], [8, 0, 1]]))

        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m2: Matrix = Matrix([[1, 1], [1, 1]])
            m3: Matrix = m1 - m2
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m3: Matrix = m1 - 7

    def test_isub(self):
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [1, 1]])
        m1 -= m2
        self.assertEqual(m1, np.array([[0, 0], [0, 0]]))
        m1: Matrix = Matrix([[1, -1], [1, 1]])
        m2: Matrix = Matrix([[1, 1], [-1, 1]])
        m1 -= m2
        self.assertEqual(m1, np.array([[0, -2], [2, 0]]))
        m1: Matrix = Matrix([[1, 3, 2], [9, 1, 2]])
        m2: Matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        m1 -= m2
        self.assertEqual(m1, np.array([[0, 2, 1], [8, 0, 1]]))

        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m2: Matrix = Matrix([[1, 1], [1, 1]])
            m1 -= m2
            m1: Matrix = Matrix([[1, 1, 2], [1, 1, 2]])
            m1 -= 7

    def test_mul(self):
        m1: Matrix = Matrix([[3, 2], [1, 2]])
        m2: Matrix = Matrix([[3, 2], [1, 2]])
        self.assertEqual(m1 * m2, np.array([[11, 10], [5, 6]]))
        m1: Matrix = Matrix([[3, 2, 1], [1, 2, 1]])
        m2: Matrix = Matrix([[3, 2], [1, 2], [5, 4]])
        self.assertEqual(m1 * m2, np.array([[16, 14], [10, 10]]))
        m1: Matrix = Matrix([[3, 2], [1, 2]])
        m2: Matrix = Matrix.create_identity_matrix(2)
        self.assertEqual(m1 * m2, m1)
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        sc: float = 5.01
        self.assertEqual(m1 * sc, np.array([[5.01, 5.01], [5.01, 5.01]]))
        self.assertEqual(sc * m1, np.array([[5.01, 5.01], [5.01, 5.01]]))

        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[3, 2], [1, 2]])
            m2: Matrix = Matrix([[3, 2], [1, 2], [5, 4]])
            m1 * m2
            m1 * "5"
            "5" * m1

    def test_imul(self):
        m1: Matrix = Matrix([[3, 2], [1, 2]])
        m2: Matrix = Matrix([[3, 2], [1, 2]])
        m1 *= m2
        self.assertEqual(m1, np.array([[11, 10], [5, 6]]))
        m1: Matrix = Matrix([[3, 2, 1], [1, 2, 1]])
        m2: Matrix = Matrix([[3, 2], [1, 2], [5, 4]])
        m1 *= m2
        self.assertEqual(m1, np.array([[16, 14], [10, 10]]))
        m1: Matrix = Matrix([[3, 2], [1, 2]])
        m2: Matrix = Matrix.create_identity_matrix(2)
        m1 *= m2
        self.assertEqual(m1, m1)
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        sc: float = 5.01
        m1 *= sc
        self.assertEqual(m1, np.array([[5.01, 5.01], [5.01, 5.01]]))

        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[3, 2], [1, 2]])
            m2: Matrix = Matrix([[3, 2], [1, 2], [5, 4]])
            m1 *= m2
            m1 *= "5"

    def test_truediv(self):
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        sc: float = 5
        self.assertEqual(m1 / sc, np.array([[.2, .2], [.2, .2]]))
        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[1, 1], [1, 1]])
            sc: float = 0
            m1 / sc
            m1 / m1
            m1 / "5"

    def test_itruediv(self):
        m1: Matrix = Matrix([[1, 1], [1, 1]])
        sc: float = 5
        m1 /= sc
        self.assertEqual(m1, np.array([[.2, .2], [.2, .2]]))
        with self.assertRaises(MathError):
            m1: Matrix = Matrix([[1, 1], [1, 1]])
            sc: float = 0
            m1 /= sc
            m1 /= m1
            m1 /= "5"

    def test_pow(self):
        m1: Matrix = Matrix([[2, 2], [2, 2]])
        self.assertEqual(m1 ** 5, np.array([[512, 512], [512, 512]]))
        with self.assertRaises(MathError):
            m1 ** -1
            m1 ** .5
            m1 ** "5"
            m1: Matrix = Matrix([[3, 2], [1, 2], [5, 4]])
            m1 ** 25

    def test_ipow(self):
        m1: Matrix = Matrix([[2, 2], [2, 2]])
        m1 **= 5
        self.assertEqual(m1, np.array([[512, 512], [512, 512]]))
        with self.assertRaises(MathError):
            m1 **= -1
            m1 **= .5
            m1 **= "5"
            m1: Matrix = Matrix([[3, 2], [1, 2], [5, 4]])
            m1 **= 25
