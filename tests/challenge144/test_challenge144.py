""" Tests for challenge144 """
from robber import expect
from pemjh.challenge144 import main


def test_challenge144():
    """ Regression testing challenge144 """
    expect(main(1)).to.eq(None)


def test_challenge144_example():
    expect(main(2)).to.eq(None)
