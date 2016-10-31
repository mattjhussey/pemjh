""" Tests for challenge46 """
from robber import expect
from pemjh.challenge46 import main


def test_challenge46():
    """ Regression testing challenge46 """
    expect(main()).to.eq(5777)
