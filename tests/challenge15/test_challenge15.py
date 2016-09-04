""" Tests for challenge15 """
from robber import expect
from pemjh.challenge15 import main


def test_challenge15():
    """ Regression testing challenge15 """
    expect(main(1)).to.eq(None)


def test_challenge15_example():
    expect(main(2)).to.eq(None)
