""" Tests for challenge145 """
from robber import expect
from pemjh.challenge145 import main


def test_challenge145():
    """ Regression testing challenge145 """
    expect(main()).to.eq(608720)
