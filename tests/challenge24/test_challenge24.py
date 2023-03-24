""" Tests for challenge24 """
from robber import expect
from pemjh.challenge24 import main


def test_challenge24():
    """ Regression testing challenge24 """
    expect(main()).to.eq(2783915460)
