""" Tests for challenge90 """
from pemjh.challenge90 import main


def test_challenge90():
    """ Regression testing challenge90 """
    assert main() == 1217
