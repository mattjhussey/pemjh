""" Tests for challenge34 """
from robber import expect
from pemjh.challenge34 import main


def test_challenge34():
    """ Regression testing challenge34 """
    expect(main()).to.eq(40730)
