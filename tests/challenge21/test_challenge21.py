""" Tests for challenge21 """
from robber import expect
from pemjh.challenge21 import main


def test_challenge21():
    """ Regression testing challenge21 """
    expect(main()).to.eq(31626)
