import pytest

from pylix.errors import ArgumentError, StateError, MathError
from pylix.algebra import Polynomial

def test___init__():
    p: Polynomial = Polynomial(2, [2, 0, 1])
    p: Polynomial = Polynomial(3, [4, 0, 0, 1])
    p: Polynomial = Polynomial(1, [1])
    p: Polynomial = Polynomial(3, (2, 1, -581))

    with pytest.raises(ArgumentError):
        p: Polynomial = Polynomial("a", [4, "d"])
        p: Polynomial = Polynomial(1, [4, "d"])
        p: Polynomial = Polynomial(1, [4, 1, 1])
        p: Polynomial = Polynomial(1, [4, True])
        p: Polynomial = Polynomial(1, None)

def test_generate_polynomial():
    s: str = Polynomial.generate_polynome(1, [1, 0])
    assert s == "1 * x"
    s: str = Polynomial.generate_polynome(2, [1, 1, 1])
    assert s == "1 * x**2 + 1 * x + 1"

    with pytest.raises(ArgumentError):
        Polynomial.generate_polynome("a", [1, 1])
        Polynomial.generate_polynome(1, [1, "a"])
        Polynomial.generate_polynome(1, [1, None])

def test_y_at_x():
    p: Polynomial = Polynomial(2, (2, 0, 1))
    assert p.y_at_x(2) == 9
    assert p.y_at_x(3) == 19
    assert p.y_at_x(2.5) == 13.5

    with pytest.raises(ArgumentError):
        p.y_at_x("a")
        p.y_at_x(["a"])
        p.y_at_x([1])
        p.y_at_x(None)

def test_area():
    p: Polynomial = Polynomial(1, (1, 0))
    assert p.area(0, 1) == 0.5
    assert p.area(0, 2) == 2
    assert p.area(0, 3.5) == 6.125
    assert p.area(3.5, 4) == 1.875

    with pytest.raises(ArgumentError):
        p.area("a", "a")
        p.area((["a"]), 2)
        p.area(False, 3)

def test_get_roots():
    p: Polynomial = Polynomial(1, [1])
    roots: tuple = p.get_roots()
    assert roots == (0,)
    p: Polynomial = Polynomial(2, [-1, 0, 1])
    roots: tuple = p.get_roots()
    assert roots == (-1, 1)

def test_derivative():
    p: Polynomial = Polynomial(2, (-1, 0, 1))
    assert p.get_derivative() == Polynomial(1, [-2, 0])
    p: Polynomial = Polynomial(1, (1, 0))
    assert p.get_derivative() == Polynomial(0, [1])
    p: Polynomial = Polynomial(1, [-2])
    assert p.get_derivative() == Polynomial(0, [-2])
    p: Polynomial = Polynomial(2, (-1, 0, 1))
    assert p.get_derivative(2) == Polynomial(0, [-2])

    with pytest.raises(ArgumentError):
        p.get_derivative("a")

    with pytest.raises(MathError):
        p.get_derivative(0)
        p.get_derivative(-1)

def test_get_local_maximum():
    p: Polynomial = Polynomial(2, (-1, 0, 1))
    maximums: list = p.get_local_maximum()
    assert maximums == [(0, 1)]

def test_get_local_minimum():
    p: Polynomial = Polynomial(2, (1, 0, 1))
    minimums: list = p.get_local_minimum()
    assert minimums == [(0, 1)]

def test_get_infliction_point():
    p: Polynomial = Polynomial(3, [1])
    infliction_points = p.get_infliction_point()
    assert infliction_points == [(0, 0)]

def test_copy():
    p: Polynomial = Polynomial(3, (2, 1, -581))
    assert id(p) != id(p.copy())

def test_limit_infinity():
    p: Polynomial = Polynomial(2, (2,))
    assert p.limit_infinity() == 1
    assert p.limit_infinity(False) == 1
    p: Polynomial = Polynomial(3, (2,))
    assert p.limit_infinity() == 1
    assert p.limit_infinity(False) == -1
    p: Polynomial = Polynomial(2, (-2,))
    assert p.limit_infinity() == -1
    assert p.limit_infinity(False) == -1
    p: Polynomial = Polynomial(3, (-2,))
    assert p.limit_infinity() == -1
    assert p.limit_infinity(False) == 1

