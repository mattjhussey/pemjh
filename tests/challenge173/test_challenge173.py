""" Tests for challenge173 """
from robber import expect
from pemjh.challenge173 import main


def test_challenge173():
    """ Regression testing challenge173 """
    expect(main(1)).to.eq(None)


def test_challenge173_example():
    expect(main(2)).to.eq(None)
