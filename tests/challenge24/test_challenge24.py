""" Tests for challenge24 """
from robber import expect
from pemjh.challenge24 import main


def test_challenge24():
    """ Regression testing challenge24 """
    expect(main(1)).to.eq(None)


def test_challenge24_example():
    expect(main(2)).to.eq(None)
