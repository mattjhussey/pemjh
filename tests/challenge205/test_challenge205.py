""" Tests for challenge205 """
from robber import expect
from pemjh.challenge205 import main


def test_challenge205():
    """ Regression testing challenge205 """
    expect(main(1)).to.eq(None)


def test_challenge205_example():
    expect(main(2)).to.eq(None)
