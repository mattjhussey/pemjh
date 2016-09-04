""" Tests for challenge70 """
from robber import expect
from pemjh.challenge70 import main


def test_challenge70():
    """ Regression testing challenge70 """
    expect(main(1)).to.eq(None)


def test_challenge70_example():
    expect(main(2)).to.eq(None)
