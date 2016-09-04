""" Tests for challenge118 """
from robber import expect
from pemjh.challenge118 import main


def test_challenge118():
    """ Regression testing challenge118 """
    expect(main(1)).to.eq(None)


def test_challenge118_example():
    expect(main(2)).to.eq(None)
