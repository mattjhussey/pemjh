""" Tests for challenge105 """
from robber import expect
from pemjh.challenge105 import main


def test_challenge105():
    """ Regression testing challenge105 """
    expect(main(1)).to.eq(None)


def test_challenge105_example():
    expect(main(2)).to.eq(None)
