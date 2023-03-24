""" Tests for challenge11 """
from robber import expect
from pemjh.challenge11 import main


def test_challenge11():
    """ Regression testing challenge11 """
    expect(main()).to.eq(70600674)
