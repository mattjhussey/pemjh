""" Tests for challenge28 """
from robber import expect
from pemjh.challenge28 import main


def test_challenge28():
    """ Regression testing challenge28 """
    expect(main(1)).to.eq(None)


def test_challenge28_example():
    expect(main(2)).to.eq(None)
