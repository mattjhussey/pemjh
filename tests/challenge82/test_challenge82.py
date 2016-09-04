""" Tests for challenge82 """
from robber import expect
from pemjh.challenge82 import main


def test_challenge82():
    """ Regression testing challenge82 """
    expect(main(1)).to.eq(None)


def test_challenge82_example():
    expect(main(2)).to.eq(None)
