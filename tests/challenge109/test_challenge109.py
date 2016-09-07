""" Tests for challenge109 """
from robber import expect
from pemjh.challenge109 import main


def test_challenge109():
    """ Regression testing challenge109 """
    expect(main()).to.eq(38182)
