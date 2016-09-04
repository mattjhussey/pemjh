""" Tests for challenge243 """
from robber import expect
from pemjh.challenge243 import main


def test_challenge243():
    """ Regression testing challenge243 """
    expect(main(1)).to.eq(None)


def test_challenge243_example():
    expect(main(2)).to.eq(None)
