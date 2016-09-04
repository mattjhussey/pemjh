""" Tests for challenge51 """
from robber import expect
from pemjh.challenge51 import main


def test_challenge51():
    """ Regression testing challenge51 """
    expect(main(1)).to.eq(None)


def test_challenge51_example():
    expect(main(2)).to.eq(None)
