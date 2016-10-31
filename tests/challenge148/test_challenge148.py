""" Tests for challenge148 """
from robber import expect
from pemjh.challenge148 import main


def test_challenge148():
    """ Regression testing challenge148 """
    expect(main()).to.eq(2129970655314432)
