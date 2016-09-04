""" Tests for challenge46 """
from robber import expect
from pemjh.challenge46 import main


def test_challenge46():
    """ Regression testing challenge46 """
    expect(main(1)).to.eq(None)


def test_challenge46_example():
    expect(main(2)).to.eq(None)
