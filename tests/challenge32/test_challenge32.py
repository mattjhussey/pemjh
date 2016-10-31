""" Tests for challenge32 """
from robber import expect
from pemjh.challenge32 import main


def test_challenge32():
    """ Regression testing challenge32 """
    expect(main()).to.eq(45228)
