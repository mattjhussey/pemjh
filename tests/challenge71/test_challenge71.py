""" Tests for challenge71 """
from robber import expect
from pemjh.challenge71 import main


def test_challenge71():
    """ Regression testing challenge71 """
    expect(main(1)).to.eq(None)


def test_challenge71_example():
    expect(main(2)).to.eq(None)
