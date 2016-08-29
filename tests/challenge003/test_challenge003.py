""" Tests for challenge003 """
from pemjh.challenge003 import main


def test_challenge003():
    """ Regression testing challenge003 """
    assert main(600851475143) == 6857


def test_challenge003_example():
    assert main(13195) == 29
