""" Tests for challenge002 """
from pemjh.challenge002 import main


def test_challenge002():
    """ Regression testing challenge002 """
    assert main(4000000) == 4613732


def test_challenge002_example():
    assert main(100) == 44
