""" Tests for challenge48 """
from robber import expect
from pemjh.challenge48 import main


def test_challenge48():
    """ Regression testing challenge48 """
    expect(main(1)).to.eq(None)


def test_challenge48_example():
    expect(main(2)).to.eq(None)
