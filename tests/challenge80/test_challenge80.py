""" Tests for challenge80 """
from robber import expect
from pemjh.challenge80 import main


def test_challenge80():
    """ Regression testing challenge80 """
    expect(main(1)).to.eq(None)


def test_challenge80_example():
    expect(main(2)).to.eq(None)
