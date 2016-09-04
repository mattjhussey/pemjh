""" Tests for challenge64 """
from robber import expect
from pemjh.challenge64 import main


def test_challenge64():
    """ Regression testing challenge64 """
    expect(main(1)).to.eq(None)


def test_challenge64_example():
    expect(main(2)).to.eq(None)
