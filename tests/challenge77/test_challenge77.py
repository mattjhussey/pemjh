""" Tests for challenge77 """
from robber import expect
from pemjh.challenge77 import main


def test_challenge77():
    """ Regression testing challenge77 """
    expect(main(1)).to.eq(None)


def test_challenge77_example():
    expect(main(2)).to.eq(None)
