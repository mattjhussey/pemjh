""" Tests for challenge216 """
from robber import expect
from pemjh.challenge216 import main


def test_challenge216():
    """ Regression testing challenge216 """
    expect(main()).to.eq(5437849)
