""" Tests for challenge110 """
from robber import expect
from pemjh.challenge110 import main


def test_challenge110():
    """ Regression testing challenge110 """
    expect(main(1)).to.eq(None)


def test_challenge110_example():
    expect(main(2)).to.eq(None)
