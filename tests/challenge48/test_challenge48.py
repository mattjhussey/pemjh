""" Tests for challenge48 """
from robber import expect
from pemjh.challenge48 import main


def test_challenge48():
    """ Regression testing challenge48 """
    expect(main()).to.eq(9110846700)
