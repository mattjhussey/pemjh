""" Tests for challenge36 """
from robber import expect
from pemjh.challenge36 import main


def test_challenge36():
    """ Regression testing challenge36 """
    expect(main(1)).to.eq(None)


def test_challenge36_example():
    expect(main(2)).to.eq(None)
