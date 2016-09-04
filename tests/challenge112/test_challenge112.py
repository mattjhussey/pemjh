""" Tests for challenge112 """
from robber import expect
from pemjh.challenge112 import main


def test_challenge112():
    """ Regression testing challenge112 """
    expect(main(1)).to.eq(None)


def test_challenge112_example():
    expect(main(2)).to.eq(None)
