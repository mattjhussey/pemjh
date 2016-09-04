""" Tests for challenge13 """
from robber import expect
from pemjh.challenge13 import main


def test_challenge13():
    """ Regression testing challenge13 """
    expect(main(1)).to.eq(None)


def test_challenge13_example():
    expect(main(2)).to.eq(None)
