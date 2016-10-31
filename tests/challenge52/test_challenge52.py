""" Tests for challenge52 """
from robber import expect
from pemjh.challenge52 import main


def test_challenge52():
    """ Regression testing challenge52 """
    expect(main()).to.eq(142857)
