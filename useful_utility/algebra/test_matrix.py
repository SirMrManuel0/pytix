import unittest
import numpy as np

from useful_utility.algebra import Matrix
from useful_utility.errors import *

class TestMatrix(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Matrix(2, 2, [[1, 2], [1, 2]]),
                         Matrix(2, 2, [[1, 2], [1, 2]]))
        self.assertEqual(Matrix(2, 2, [[1, 2], [1, 2]]),
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
