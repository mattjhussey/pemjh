""" Tests for challenge80 """
from robber import expect
from pemjh.challenge80 import main


def test_challenge80():
    """ Regression testing challenge80 """
    expect(main()).to.eq(40886)
