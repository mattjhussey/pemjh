""" Tests for challenge130 """
from robber import expect
from pemjh.challenge130 import main


def test_challenge130():
    """ Regression testing challenge130 """
    expect(main()).to.eq(149253)
