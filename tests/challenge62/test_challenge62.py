""" Tests for challenge62 """
from robber import expect
from pemjh.challenge62 import main


def test_challenge62():
    """ Regression testing challenge62 """
    expect(main()).to.eq(127035954683)
