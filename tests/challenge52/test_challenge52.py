""" Tests for challenge52 """
from robber import expect
from pemjh.challenge52 import main


def test_challenge52():
    """ Regression testing challenge52 """
    expect(main(1)).to.eq(None)


def test_challenge52_example():
    expect(main(2)).to.eq(None)
