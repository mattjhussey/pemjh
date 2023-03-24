""" Tests for challenge164 """
from robber import expect
from pemjh.challenge164 import main


def test_challenge164():
    """ Regression testing challenge164 """
    expect(main()).to.eq(378158756814587)
