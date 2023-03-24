""" Tests for challenge120 """
from robber import expect
from pemjh.challenge120 import main


def test_challenge120():
    """ Regression testing challenge120 """
    expect(main()).to.eq(333082500)
