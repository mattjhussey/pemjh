""" Tests for challenge76 """
from robber import expect
from pemjh.challenge76 import main


def test_challenge76():
    """ Regression testing challenge76 """
    expect(main()).to.eq(190569291)
