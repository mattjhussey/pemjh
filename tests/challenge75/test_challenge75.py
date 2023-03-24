""" Tests for challenge75 """
from robber import expect
from pemjh.challenge75 import main


def test_challenge75():
    """ Regression testing challenge75 """
    expect(main()).to.eq(161667)
