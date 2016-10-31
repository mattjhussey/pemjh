""" Tests for challenge191 """
from robber import expect
from pemjh.challenge191 import main


def test_challenge191():
    """ Regression testing challenge191 """
    expect(main()).to.eq(1918080160)
