""" Tests for challenge134 """
from robber import expect
from pemjh.challenge134 import main


def test_challenge134():
    """ Regression testing challenge134 """
    expect(main()).to.eq(18613426663617118)
