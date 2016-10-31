""" Tests for challenge93 """
from robber import expect
from pemjh.challenge93 import main


def test_challenge93():
    """ Regression testing challenge93 """
    expect(main()).to.eq(1258)
