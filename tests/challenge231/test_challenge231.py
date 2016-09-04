""" Tests for challenge231 """
from robber import expect
from pemjh.challenge231 import main


def test_challenge231():
    """ Regression testing challenge231 """
    expect(main(1)).to.eq(None)


def test_challenge231_example():
    expect(main(2)).to.eq(None)
