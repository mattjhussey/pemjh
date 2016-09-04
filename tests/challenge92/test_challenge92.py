""" Tests for challenge92 """
from robber import expect
from pemjh.challenge92 import main


def test_challenge92():
    """ Regression testing challenge92 """
    expect(main(1)).to.eq(None)


def test_challenge92_example():
    expect(main(2)).to.eq(None)
