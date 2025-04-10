import pytest

from pylix.algebra.statics import rnd, variance, average, std
from pylix.errors.useful_errors import ArgumentError

def test_rnd():
    assert 5.200_021_895 == rnd(5.200_021_895_1)
    assert 5.200_021_895 == rnd(5.200_021_894_6)
    assert 5.20002 == rnd(5.200021, 5)
    assert 5.20002 == rnd(5.200016, 5)

def test_average():
    assert 5 == average([5, 5, 5, 5, 5])
    assert 5 == average([4, 5, 5, 5, 6])
    assert 5 == average([3, 4, 5, 6, 7])
    assert 5 == average([-5, 4, 5, 6, 15])

def test_variance():
    assert 0 == variance([5, 5, 5, 5, 5])
    assert .4 == variance([4, 5, 5, 5, 6])
    assert 2 == variance([3, 4, 5, 6, 7])
    assert 40.4 == variance([-5, 4, 5, 6, 15])

def test_std():
    assert 0 == std([5, 5, 5, 5, 5])
    assert .632_455_532 == std([4, 5, 5, 5, 6])
    assert 1.414_213_562 == std([3, 4, 5, 6, 7])
    assert 6.356_099_433 == std([-5, 4, 5, 6, 15])
