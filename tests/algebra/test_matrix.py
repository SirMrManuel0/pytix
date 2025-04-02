import math

import pytest
import numpy as np

from pylix.algebra import Matrix, Vector, Axis
from pylix.algebra.statics import rnd
from pylix.errors import *


def test_init():
    assert Matrix([[1, 2], [1, 2]], 2, 2) == Matrix([[1, 2], [1, 2]], 2, 2)
    assert Matrix([[1, 2], [1, 2]], 2, 2) == np.array([[1, 2], [1, 2]])
    assert Matrix(rows=5, columns=5, default_value=1) == np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ])

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

def test_create_rotation_matrix_2D():
    m1 = Matrix.create_rotation_matrix_2D(90)
    v1 = Vector(coordinates=[1, 0])

    expected = Vector([0, 1])
    assert m1 == np.array([[0, -1], [1, 0]])
    result = m1 * v1
    assert result == expected

    m1 = Matrix.create_rotation_matrix_2D(180)
    v1 = Vector(coordinates=[1, 0])

    expected = Vector([-1, 0])

    result = m1 * v1
    assert result == expected

    m1 = Matrix.create_rotation_matrix_2D(270)
    v1 = Vector(coordinates=[1, 0])

    expected = Vector([0, -1])

    result = m1 * v1
    assert result == expected

    m1 = Matrix.create_rotation_matrix_2D(360)
    v1 = Vector(coordinates=[1, 0])

    expected = Vector([1, 0])

    result = m1 * v1
    assert result == expected

    m1 = Matrix.create_rotation_matrix_2D(45)
    v1 = Vector(coordinates=[1, 0])

    expected = Vector([rnd(math.sqrt(2) / 2), rnd(math.sqrt(2) / 2)])

    result = m1 * v1
    assert result == expected

    with pytest.raises(ArgumentError):
        Matrix.create_rotation_matrix_2D(-10)
        Matrix.create_rotation_matrix_2D(400)
        Matrix.create_rotation_matrix_2D("90")

def test_create_rotation_matrix_3D():
    m = Matrix.create_rotation_matrix_3D(90, Axis.X)
    v = Vector([0, 1, 0])

    expected = Vector([0, 0, 1])

    result = m * v
    assert result == expected

    m = Matrix.create_rotation_matrix_3D(90, Axis.Y)
    v = Vector([1, 0, 0])

    expected = Vector([0, 0, -1])

    result = m * v
    assert result == expected

    m = Matrix.create_rotation_matrix_3D(90, Axis.Z)
    v = Vector([1, 0, 0])

    expected = Vector([0, 1, 0])

    result = m * v
    assert result == expected

    m = Matrix.create_rotation_matrix_3D(360, Axis.Y)
    v = Vector([1, 0, 0])

    expected = Vector([1, 0, 0])

    result = m * v
    assert result == expected

    with pytest.raises(ArgumentError):
        Matrix.create_rotation_matrix_3D(-10, Axis.X)
        Matrix.create_rotation_matrix_3D(400, Axis.Y)
        Matrix.create_rotation_matrix_3D(90, "invalid_axis")

def test___iter__():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    for l in m:
        assert all(l == [1, 2]) or all(l == [3, 4])
        for n in l:
            assert n in [1, 2, 3, 4]

def test___getitem__():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m[0][1] == 2
    assert m[-1][-1] == 4
    with pytest.raises(ArgumentError):
        a = m["1"][1]
        a = m[0][5]
        a = m[0][None]

def test___setitem__():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    m[0][1] = 3
    assert m[0][1] == 3

    with pytest.raises(ArgumentError):
        m["1"][1] = 2
        m[0][5] = 3
        m[0][None] = 4
        m[0][1] = "2"

def test_eq():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    n: Matrix = Matrix([[1, 2], [3, 4]])
    b = m == n
    assert b is True
    m: Matrix = Matrix([[1, 2], [3, 4]])
    n: list = [[1, 2], [3, 4]]
    b = m == n
    assert b is True
    m: Matrix = Matrix([[1, 2], [3, 4]])
    n: tuple = ((1, 2), (3, 4))
    b = m == n
    m: Matrix = Matrix([[1, 2], [3, 4]])
    n: np.ndarray = np.array([[1, 2], [3, 4]])
    b = m == n
    assert b is True
    m: Matrix = Matrix([[1, 2], [3, 4]])
    n: str = "A"
    b = m == n
    assert b is False

def test_where():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    allowed: list = [[False, True], [True, False]]
    expected: Matrix = Matrix([[-1, 2], [3, -1]])
    assert m.where(allowed) == expected
    allowed_n: list = [[0, 1], [1, 0]]
    assert m.where(allowed_n) == expected
    allowed: Matrix = Matrix(allowed_n)
    assert m.where(allowed) == expected
    m: Matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    allowed: list = [[False, True, False], [True, False, True]]
    expected: Matrix = Matrix([[-1, 2, -1], [4, -1, 6]])
    assert m.where(allowed) == expected
    allowed_n: list = [[0, 1, 0], [1, 0, 1]]
    assert m.where(allowed_n) == expected
    allowed: Matrix = Matrix(allowed_n)
    assert m.where(allowed) == expected

def test_max_in_column():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.max_in_column(1) == 4

def test_min_in_column():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.min_in_column(0) == 1

def test_max_in_row():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.max_in_row(0) == 2

def test_min_in_row():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.min_in_row(1) == 3

def test_sum_in_column():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.sum_in_column(1) == 6

def test_sum_in_row():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.sum_in_row(0) == 3

def test_max():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.max() == 4

def test_min():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.min() == 1

def test_sum():
    m: Matrix = Matrix([[1, 2], [3, 4]])
    assert m.sum() == 10
