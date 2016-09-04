""" Tests for challenge93 """
from robber import expect
from pemjh.challenge93 import main


def test_challenge93():
    """ Regression testing challenge93 """
    expect(main(1)).to.eq(None)


def test_challenge93_example():
    expect(main(2)).to.eq(None)
