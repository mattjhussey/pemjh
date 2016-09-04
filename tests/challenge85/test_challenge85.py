""" Tests for challenge85 """
from robber import expect
from pemjh.challenge85 import main


def test_challenge85():
    """ Regression testing challenge85 """
    expect(main(1)).to.eq(None)


def test_challenge85_example():
    expect(main(2)).to.eq(None)
