""" Tests for challenge60 """
from robber import expect
from pemjh.challenge60 import main


def test_challenge60():
    """ Regression testing challenge60 """
    expect(main(1)).to.eq(None)


def test_challenge60_example():
    expect(main(2)).to.eq(None)
