""" Tests for challenge75 """
from robber import expect
from pemjh.challenge75 import main


def test_challenge75():
    """ Regression testing challenge75 """
    expect(main(1)).to.eq(None)


def test_challenge75_example():
    expect(main(2)).to.eq(None)
