""" Tests for challenge35 """
from robber import expect
from pemjh.challenge35 import main


def test_challenge35():
    """ Regression testing challenge35 """
    expect(main()).to.eq(55)
