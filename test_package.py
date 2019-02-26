import sys
from unittest import SkipTest


def test_add():
    assert 1 + 1 == 2


def test_add2():
    assert 1 + 1 == 2


def test_add3():
    assert 1 + 1 == 2
    # fail in python 2 only
    assert sys.version_info.major == 3


def test_add4():
    assert 1 + 1 == 2


def test_add5():
    assert 1 + 1 == 2


def test_add6():
    assert 1 + 1 == 2


def test_add7():
    assert 1 + 1 == 2
    assert 1 + 1 == 2
    assert 1 + 1 == 2
    assert 1 + 1 == 2
    assert 1 + 2 == 3


def test_skip():
    raise SkipTest('lol')
