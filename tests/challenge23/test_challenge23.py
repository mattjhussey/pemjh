""" Tests for challenge23 """
from robber import expect
from pemjh.challenge23 import main


def test_challenge23():
    """ Regression testing challenge23 """
    expect(main()).to.eq(4179871)
