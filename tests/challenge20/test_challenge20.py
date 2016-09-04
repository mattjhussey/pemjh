""" Tests for challenge20 """
from robber import expect
from pemjh.challenge20 import main


def test_challenge20():
    """ Regression testing challenge20 """
    expect(main(1)).to.eq(None)


def test_challenge20_example():
    expect(main(2)).to.eq(None)
