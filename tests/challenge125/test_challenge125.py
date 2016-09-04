""" Tests for challenge125 """
from robber import expect
from pemjh.challenge125 import main


def test_challenge125():
    """ Regression testing challenge125 """
    expect(main(1)).to.eq(None)


def test_challenge125_example():
    expect(main(2)).to.eq(None)
