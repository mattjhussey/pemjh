""" Tests for challenge58 """
from robber import expect
from pemjh.challenge58 import main


def test_challenge58():
    """ Regression testing challenge58 """
    expect(main(1)).to.eq(None)


def test_challenge58_example():
    expect(main(2)).to.eq(None)
