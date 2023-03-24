""" Tests for challenge71 """
from robber import expect
from pemjh.challenge71 import main


def test_challenge71():
    """ Regression testing challenge71 """
    expect(main()).to.eq(428570)
