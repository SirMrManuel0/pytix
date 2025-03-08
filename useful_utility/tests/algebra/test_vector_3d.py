import pytest
from useful_utility.algebra import Vector3D, Vector, Matrix
from useful_utility.errors import ArgumentError


def test_init():
    v: Vector3D = Vector3D([1, 1, 1])
    with pytest.raises(ArgumentError):
        v: Vector3D = Vector3D("a")
        v: Vector3D = Vector3D([0])
        v: Vector3D = Vector3D(0)
        v: Vector3D = Vector3D("0")


def test_from_vector():
    v: Vector3D = Vector3D.from_vector(Vector([1, 1, 1]))
    with pytest.raises(ArgumentError):
        v: Vector3D = Vector3D.from_vector(Vector([1, 1]))
        v: Vector3D = Vector3D.from_vector([1, 1])


def test_from_matrix():
    v: Vector3D = Vector3D.from_matrix(Matrix([[1], [1], [1]]))
    with pytest.raises(ArgumentError):
        v: Vector3D = Vector3D.from_matrix(Matrix([[1], [1]]))
        v: Vector3D = Vector3D.from_matrix([1, 1])

def test_cross():
    v1: Vector3D = Vector3D([1, 0, 0])
    v2: Vector3D = Vector3D([0, 1, 0])
    v3: Vector3D = Vector3D([0, 0, 1])
    v_cross = v1.cross(v2)
    assert v_cross == v3

    with pytest.raises(ArgumentError):
        v1.cross("a")
        v1.cross(0)
        v1.cross([0])
