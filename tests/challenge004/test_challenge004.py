""" Tests for challenge004 """
from robber import expect
from pemjh.challenge004 import main


def test_challenge004():
    """ Regression testing challenge004 """
    expect(main(3)).to.eq(906609)


def test_challenge004_example():
    expect(main(2)).to.eq(9009)
