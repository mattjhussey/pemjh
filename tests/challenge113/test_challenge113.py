""" Tests for challenge113 """
from robber import expect
from pemjh.challenge113 import main


def test_challenge113():
    """ Regression testing challenge113 """
    expect(main(1)).to.eq(None)


def test_challenge113_example():
    expect(main(2)).to.eq(None)
