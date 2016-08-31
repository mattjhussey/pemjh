""" Tests for challenge91 """
from pemjh.challenge91 import main


def test_challenge91():
    """ Regression testing challenge91 """
    assert main(50) == 14234


def test_challenge91_example():
    assert main(2) == 14
