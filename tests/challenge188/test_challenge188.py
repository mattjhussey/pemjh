""" Tests for challenge188 """
from robber import expect
from pemjh.challenge188 import main


def test_challenge188():
    """ Regression testing challenge188 """
    expect(main(1)).to.eq(None)


def test_challenge188_example():
    expect(main(2)).to.eq(None)
