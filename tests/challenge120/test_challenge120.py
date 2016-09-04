""" Tests for challenge120 """
from robber import expect
from pemjh.challenge120 import main


def test_challenge120():
    """ Regression testing challenge120 """
    expect(main(1)).to.eq(None)


def test_challenge120_example():
    expect(main(2)).to.eq(None)
