""" Tests for challenge136 """
from robber import expect
from pemjh.challenge136 import main


def test_challenge136():
    """ Regression testing challenge136 """
    expect(main(1)).to.eq(None)


def test_challenge136_example():
    expect(main(2)).to.eq(None)
