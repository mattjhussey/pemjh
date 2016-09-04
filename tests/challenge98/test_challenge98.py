""" Tests for challenge98 """
from robber import expect
from pemjh.challenge98 import main


def test_challenge98():
    """ Regression testing challenge98 """
    expect(main(1)).to.eq(None)


def test_challenge98_example():
    expect(main(2)).to.eq(None)
