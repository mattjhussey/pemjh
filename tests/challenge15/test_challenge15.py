""" Tests for challenge15 """
from robber import expect
from pemjh.challenge15 import main


def test_challenge15():
    """ Regression testing challenge15 """
    expect(main()).to.eq(137846528820)
