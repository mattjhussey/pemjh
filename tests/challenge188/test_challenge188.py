""" Tests for challenge188 """
from robber import expect
from pemjh.challenge188 import main


def test_challenge188():
    """ Regression testing challenge188 """
    expect(main()).to.eq(95962097)
