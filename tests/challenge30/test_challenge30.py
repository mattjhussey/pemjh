""" Tests for challenge30 """
from robber import expect
from pemjh.challenge30 import main


def test_challenge30():
    """ Regression testing challenge30 """
    expect(main(1)).to.eq(None)


def test_challenge30_example():
    expect(main(2)).to.eq(None)
