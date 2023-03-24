""" Tests for challenge18 """
from robber import expect
from pemjh.challenge18 import main


def test_challenge18():
    """ Regression testing challenge18 """
    expect(main()).to.eq(1074)
