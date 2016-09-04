""" Tests for challenge61 """
from robber import expect
from pemjh.challenge61 import main


def test_challenge61():
    """ Regression testing challenge61 """
    expect(main(1)).to.eq(None)


def test_challenge61_example():
    expect(main(2)).to.eq(None)
