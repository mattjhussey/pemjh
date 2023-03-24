""" Tests for challenge16 """
from robber import expect
from pemjh.challenge16 import main


def test_challenge16():
    """ Regression testing challenge16 """
    expect(main()).to.eq(1366)
