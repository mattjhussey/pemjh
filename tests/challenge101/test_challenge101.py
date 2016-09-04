""" Tests for challenge101 """
from robber import expect
from pemjh.challenge101 import main


def test_challenge101():
    """ Regression testing challenge101 """
    expect(main(1)).to.eq(None)


def test_challenge101_example():
    expect(main(2)).to.eq(None)
