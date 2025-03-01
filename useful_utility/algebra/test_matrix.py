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

    #def test_add(self):
    #    m1: Matrix
