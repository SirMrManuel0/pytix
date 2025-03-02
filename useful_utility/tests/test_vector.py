import pytest
from useful_utility.algebra.vector import Vector
from useful_utility.algebra.statics import rnd
from useful_utility.errors import ArgumentError, MathError

def test_init():
    Vector(5, (5, 5, 5))
    with pytest.raises(ArgumentError):
        Vector()
        Vector(5, (5, None))
        Vector(5, (5, "5"))

def test_length():
    assert Vector(2, (3, 4)).length() == 5
    assert Vector(25, [1] * 25).length() == rnd(25 ** 0.5)
    assert Vector(1, (0,)).length() == 0
    assert Vector(1, (-1,)).length() == 1

def test_add():
    assert Vector(1, (1,)) + Vector(1, (2,)) == Vector(1, (3,))
    assert Vector(2, (1, 1)) + Vector(2, (1, 1)) == Vector(2, (2, 2))
    assert Vector(2, (0, -1)) + Vector(2, (5, -3)) == Vector(2, (5, -4))
    assert Vector(2, (1, 1)) + Vector(2, (1, 0)) == Vector(2, (2, 1))
    with pytest.raises(MathError):
        Vector(2, (1, 1)) + "5"

def test_sub():
    assert Vector(2, (1, 1)) - Vector(2, (1, 1)) == Vector(2, (0, 0))
    assert Vector(2, (1, 0)) - Vector(2, (1, 1)) == Vector(2, (0, -1))
    with pytest.raises(MathError):
        Vector(2, (1, 1)) - "5"

def test_iadd():
    v1 = Vector(1, (1,))
    v1 += Vector(1, (1,))
    assert v1 == Vector(1, (2,))

def test_isub():
    v1 = Vector(2, (1, 1))
    v1 -= Vector(2, (1, 1))
    assert v1 == Vector(2, (0, 0))

def test_mul():
    assert Vector(2, (1, 1)) * Vector(2, (2, 1)) == 3
    assert Vector(2, (2, 5)) * 5 == Vector(2, (10, 25))
    with pytest.raises(MathError):
        Vector(2, (2, 5)) * "5"

def test_imul():
    v1 = Vector(2, (1, 1))
    v1 *= 5
    assert v1 == Vector(2, (5, 5))
    with pytest.raises(MathError):
        v1 *= Vector(2, (1, 1))
        v1 *= "5"

def test_div():
    with pytest.raises(MathError):
        Vector(1, (1,)) / 0
    assert Vector(1, (1,)) / 2 == Vector(2, (0.5, 0.5))
    with pytest.raises(MathError):
        Vector(1, (1,)) / "5"

def test_idiv():
    v1 = Vector(2, (1, 1))
    v1 /= 5
    assert v1 == Vector(2, (0.2, 0.2))
    with pytest.raises(MathError):
        v1 /= 0
        v1 /= "5"
