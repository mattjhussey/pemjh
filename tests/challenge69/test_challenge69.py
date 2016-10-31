""" Tests for challenge69 """
from robber import expect
from pemjh.challenge69 import main


def test_challenge69():
    """ Regression testing challenge69 """
    expect(main()).to.eq(510510)
