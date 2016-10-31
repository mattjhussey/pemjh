""" Tests for challenge36 """
from robber import expect
from pemjh.challenge36 import main


def test_challenge36():
    """ Regression testing challenge36 """
    expect(main()).to.eq(872187)
