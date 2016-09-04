""" Tests for challenge204 """
from robber import expect
from pemjh.challenge204 import main


def test_challenge204():
    """ Regression testing challenge204 """
    expect(main(1)).to.eq(None)


def test_challenge204_example():
    expect(main(2)).to.eq(None)
