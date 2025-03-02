import pytest
import numpy as np
from useful_utility.algebra import Matrix
from useful_utility.errors import *


def test_init():
    assert Matrix([[1, 2], [1, 2]], 2, 2) == Matrix([[1, 2], [1, 2]], 2, 2)
    assert Matrix([[1, 2], [1, 2]], 2, 2) == np.array([[1, 2], [1, 2]])

    with pytest.raises(ArgumentError):
        Matrix("a")
        Matrix(rows="a")
        Matrix(data="a")
        Matrix(-1)
        Matrix(rows=-1)
        Matrix(0)
        Matrix(rows=0)
        Matrix(data=["a"])


def test_set_components():
    m = Matrix([[1, 2], [1, 2]], 2, 2)
    m.set_components([[1, 1], [1, 2]])
    assert m == np.array([[1, 1], [1, 2]])

    n = np.array([[1], [0]])
    m.set_components(n)
    assert m == n
    assert m.get_dimension() == (2, 1)

    m.set_components([1, 1])
    assert m == np.array([[1], [1]])

    m.set_components([[np.float64(5.01)] * 2] * 2)
    assert m == np.array([[5.01, 5.01], [5.01, 5.01]])

    with pytest.raises(ArgumentError):
        m.set_components((1, 1))
        m.set_components(1)
        m.set_components(["a", 2])


def test_copy():
    m = Matrix([1, 2])
    v = m.copy()
    assert id(v) != id(m)


def test_create_identity_matrix():
    m = Matrix.create_identity_matrix()
    assert m == np.array([[1, 0], [0, 1]])

    with pytest.raises(ArgumentError):
        Matrix.create_identity_matrix(1.06)
        Matrix.create_identity_matrix("1.061.06")
        Matrix.create_identity_matrix([1])


def test_add():
    m1 = Matrix([[1, 1], [1, 1]])
    m2 = Matrix([[1, 1], [1, 1]])
    assert m1 + m2 == np.array([[2, 2], [2, 2]])

    with pytest.raises(MathError):
        m1 = Matrix([[1, 1, 2], [1, 1, 2]])
        m2 = Matrix([[1, 1], [1, 1]])
        _ = m1 + m2
        _ = m1 + 7


def test_mul():
    m1 = Matrix([[3, 2], [1, 2]])
    m2 = Matrix([[3, 2], [1, 2]])
    assert m1 * m2 == np.array([[11, 10], [5, 6]])

    with pytest.raises(MathError):
        m1 = Matrix([[3, 2], [1, 2]])
        m2 = Matrix([[3, 2], [1, 2], [5, 4]])
        _ = m1 * m2
        _ = m1 * "5"
        _ = "5" * m1


def test_truediv():
    m1 = Matrix([[1, 1], [1, 1]])
    sc = 5
    assert m1 / sc == np.array([[.2, .2], [.2, .2]])

    with pytest.raises(MathError):
        _ = m1 / 0
        _ = m1 / m1
        _ = m1 / "5"


def test_pow():
    m1 = Matrix([[2, 2], [2, 2]])
    assert m1 ** 5 == np.array([[512, 512], [512, 512]])

    with pytest.raises(MathError):
        _ = m1 ** -1
        _ = m1 ** .5
        _ = m1 ** "5"
        m1 = Matrix([[3, 2], [1, 2], [5, 4]])
        _ = m1 ** 25
