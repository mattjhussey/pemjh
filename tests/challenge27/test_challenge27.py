""" Tests for challenge27 """
from robber import expect
from pemjh.challenge27 import main


def test_challenge27():
    """ Regression testing challenge27 """
    expect(main()).to.eq(-59231)
