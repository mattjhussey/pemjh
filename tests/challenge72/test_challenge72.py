""" Tests for challenge72 """
from robber import expect
from pemjh.challenge72 import main


def test_challenge72():
    """ Regression testing challenge72 """
    expect(main(1)).to.eq(None)


def test_challenge72_example():
    expect(main(2)).to.eq(None)
