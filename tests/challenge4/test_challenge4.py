""" Tests for challenge4 """
from robber import expect
from pemjh.challenge4 import main


def test_challenge4():
    """ Regression testing challenge4 """
    expect(main(3)).to.eq(906609)


def test_challenge4_example():
    expect(main(2)).to.eq(9009)
