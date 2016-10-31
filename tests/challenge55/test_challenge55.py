""" Tests for challenge55 """
from robber import expect
from pemjh.challenge55 import main


def test_challenge55():
    """ Regression testing challenge55 """
    expect(main()).to.eq(249)
