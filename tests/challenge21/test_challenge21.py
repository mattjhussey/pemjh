""" Tests for challenge21 """
from robber import expect
from pemjh.challenge21 import main


def test_challenge21():
    """ Regression testing challenge21 """
    expect(main(1)).to.eq(None)


def test_challenge21_example():
    expect(main(2)).to.eq(None)
