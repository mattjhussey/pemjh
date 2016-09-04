""" Tests for challenge79 """
from robber import expect
from pemjh.challenge79 import main


def test_challenge79():
    """ Regression testing challenge79 """
    expect(main(1)).to.eq(None)


def test_challenge79_example():
    expect(main(2)).to.eq(None)
