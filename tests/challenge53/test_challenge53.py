""" Tests for challenge53 """
from robber import expect
from pemjh.challenge53 import main


def test_challenge53():
    """ Regression testing challenge53 """
    expect(main(1)).to.eq(None)


def test_challenge53_example():
    expect(main(2)).to.eq(None)
