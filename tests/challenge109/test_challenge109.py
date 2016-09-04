""" Tests for challenge109 """
from robber import expect
from pemjh.challenge109 import main


def test_challenge109():
    """ Regression testing challenge109 """
    expect(main(1)).to.eq(None)


def test_challenge109_example():
    expect(main(2)).to.eq(None)
