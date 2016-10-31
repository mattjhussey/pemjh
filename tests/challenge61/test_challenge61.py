""" Tests for challenge61 """
from robber import expect
from pemjh.challenge61 import main


def test_challenge61():
    """ Regression testing challenge61 """
    expect(main()).to.eq(28684)
