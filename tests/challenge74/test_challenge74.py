""" Tests for challenge74 """
from robber import expect
from pemjh.challenge74 import main


def test_challenge74():
    """ Regression testing challenge74 """
    expect(main(1)).to.eq(None)


def test_challenge74_example():
    expect(main(2)).to.eq(None)
