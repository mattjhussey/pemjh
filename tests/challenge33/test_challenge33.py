""" Tests for challenge33 """
from robber import expect
from pemjh.challenge33 import main


def test_challenge33():
    """ Regression testing challenge33 """
    expect(main(1)).to.eq(None)


def test_challenge33_example():
    expect(main(2)).to.eq(None)
