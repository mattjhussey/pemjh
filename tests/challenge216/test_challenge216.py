""" Tests for challenge216 """
from robber import expect
from pemjh.challenge216 import main


def test_challenge216():
    """ Regression testing challenge216 """
    expect(main(1)).to.eq(None)


def test_challenge216_example():
    expect(main(2)).to.eq(None)
