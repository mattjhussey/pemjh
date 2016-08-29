""" Tests for challenge001 """
from pemjh.challenge001 import main


def test_challenge001():
    """ Regression testing challenge001 """
    dir(main)
    assert main(1000) == 233168


def test_challenge001_example():
    assert main(10) == 23
