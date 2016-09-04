""" Tests for challenge130 """
from robber import expect
from pemjh.challenge130 import main


def test_challenge130():
    """ Regression testing challenge130 """
    expect(main(1)).to.eq(None)


def test_challenge130_example():
    expect(main(2)).to.eq(None)
