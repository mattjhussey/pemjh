""" Tests for challenge27 """
from robber import expect
from pemjh.challenge27 import main


def test_challenge27():
    """ Regression testing challenge27 """
    expect(main(1)).to.eq(None)


def test_challenge27_example():
    expect(main(2)).to.eq(None)
