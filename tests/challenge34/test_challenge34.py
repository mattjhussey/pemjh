""" Tests for challenge34 """
from robber import expect
from pemjh.challenge34 import main


def test_challenge34():
    """ Regression testing challenge34 """
    expect(main(1)).to.eq(None)


def test_challenge34_example():
    expect(main(2)).to.eq(None)
