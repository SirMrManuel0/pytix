import pytest
from useful_utility.algebra.vector import Vector
from useful_utility.algebra.statics import rnd
from useful_utility.errors import ArgumentError, MathError

def test_init():
    Vector((5, 5, 5))
    with pytest.raises(ArgumentError):
        Vector()
        Vector((5, None))
        Vector((5, "5"))

def test_length():
    assert Vector((3, 4)).length() == 5
    assert Vector([1] * 25).length() == rnd(25 ** 0.5)
    assert Vector((0,)).length() == 0
    assert Vector((-1,)).length() == 1

def test_add():
    assert Vector((1,)) + Vector((2,)) == Vector((3,))
    assert Vector((1, 1)) + Vector((1, 1)) == Vector((2, 2))
    assert Vector((0, -1)) + Vector((5, -3)) == Vector((5, -4))
    assert Vector((1, 1)) + Vector((1, 0)) == Vector((2, 1))
    with pytest.raises(MathError):
        Vector((1, 1)) + "5"

def test_sub():
    assert Vector((1, 1)) - Vector((1, 1)) == Vector((0, 0))
    assert Vector((1, 0)) - Vector((1, 1)) == Vector((0, -1))
    with pytest.raises(MathError):
        Vector((1, 1)) - "5"

def test_iadd():
    v1 = Vector((1,))
    v1 += Vector((1,))
    assert v1 == Vector((2,))

def test_isub():
    v1 = Vector((1, 1))
    v1 -= Vector((1, 1))
    assert v1 == Vector((0, 0))

def test_mul():
    assert Vector((1, 1)) * Vector((2, 1)) == 3
    assert Vector((2, 5)) * 5 == Vector((10, 25))
    with pytest.raises(MathError):
        Vector((2, 5)) * "5"

def test_imul():
    v1 = Vector((1, 1))
    v1 *= 5
    assert v1 == Vector((5, 5))
    with pytest.raises(MathError):
        v1 *= Vector((1, 1))
        v1 *= "5"

def test_div():
    with pytest.raises(MathError):
        Vector((1,)) / 0
    assert Vector((1,)) / 2 == Vector((0.5, 0.5))
    with pytest.raises(MathError):
        Vector((1,)) / "5"

def test_idiv():
    v1 = Vector((1, 1))
    v1 /= 5
    assert v1 == Vector((0.2, 0.2))
    with pytest.raises(MathError):
        v1 /= 0
        v1 /= "5"

def test_cross():
    v1: Vector = Vector([1, 0, 0])
    v2: Vector = Vector([0, 1, 0])
    v3: Vector = Vector([0, 0, 1])
    v_cross = v1.cross(v2)
    assert v_cross == v3

    with pytest.raises(ArgumentError):
        v1.cross("a")
        v1.cross(0)
        v1.cross([0])
        v1.cross(Vector([1, 1, 1, 1]))
        v1: Vector = Vector([1, 1, 1, 1])
        v1.cross(Vector([1, 1, 1, 1]))
        v1.cross(Vector([1, 1, 1]))

def test___iter__():
    m: Vector = Vector([1, 2, 3, 4])
    for n in m:
        assert n in [1, 2, 3, 4]

def test___getitem__():
    v: Vector = Vector([1, 2, 3])
    assert v[0] == 1
    assert v[-1] == 3

def test___setitem__():
    v: Vector = Vector([1, 2, 3])
    v[1] = 3
    assert v[1] == 3

def test_where():
    m: Vector = Vector([1, 2])
    allowed: list = [False, True]
    expected: Vector = Vector([-1, 2])
    assert m.where(allowed) == expected
    allowed_n: list = [0, 1]
    assert m.where(allowed_n) == expected
    allowed: Vector = Vector(allowed_n)
    assert m.where(allowed) == expected

