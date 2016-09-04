""" Tests for challenge14 """
from robber import expect
from pemjh.challenge14 import main


def test_challenge14():
    """ Regression testing challenge14 """
    expect(main(1)).to.eq(None)


def test_challenge14_example():
    expect(main(2)).to.eq(None)
