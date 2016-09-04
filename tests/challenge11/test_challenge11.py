""" Tests for challenge11 """
from robber import expect
from pemjh.challenge11 import main


def test_challenge11():
    """ Regression testing challenge11 """
    expect(main(1)).to.eq(None)


def test_challenge11_example():
    expect(main(2)).to.eq(None)
