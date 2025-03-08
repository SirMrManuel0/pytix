import pytest
from useful_utility.algebra import Vector2D, Vector, Matrix
from useful_utility.errors import ArgumentError


def test_init():
    v: Vector2D = Vector2D([1, 1])
    with pytest.raises(ArgumentError):
        v: Vector2D = Vector2D("a")
        v: Vector2D = Vector2D([0])
        v: Vector2D = Vector2D(0)
        v: Vector2D = Vector2D("0")

def test_from_vector():
    v: Vector2D = Vector2D.from_vector(Vector([1, 1]))
    with pytest.raises(ArgumentError):
        v: Vector2D = Vector2D.from_vector(Vector([1, 1, 1]))
        v: Vector2D = Vector2D.from_vector([1, 1])

def test_from_matrix():
    v: Vector2D = Vector2D.from_matrix(Matrix([[1], [1]]))
    with pytest.raises(ArgumentError):
        v: Vector2D = Vector2D.from_matrix(Matrix([[1], [1], [1]]))
        v: Vector2D = Vector2D.from_matrix([1, 1])
