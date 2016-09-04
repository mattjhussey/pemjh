""" Tests for challenge73 """
from robber import expect
from pemjh.challenge73 import main


def test_challenge73():
    """ Regression testing challenge73 """
    expect(main(1)).to.eq(None)


def test_challenge73_example():
    expect(main(2)).to.eq(None)
