""" Tests for challenge85 """
from robber import expect
from pemjh.challenge85 import main


def test_challenge85():
    """ Regression testing challenge85 """
    expect(main()).to.eq(2772)
