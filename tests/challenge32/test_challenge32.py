""" Tests for challenge32 """
from robber import expect
from pemjh.challenge32 import main


def test_challenge32():
    """ Regression testing challenge32 """
    expect(main(1)).to.eq(None)


def test_challenge32_example():
    expect(main(2)).to.eq(None)
