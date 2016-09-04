""" Tests for challenge76 """
from robber import expect
from pemjh.challenge76 import main


def test_challenge76():
    """ Regression testing challenge76 """
    expect(main(1)).to.eq(None)


def test_challenge76_example():
    expect(main(2)).to.eq(None)
