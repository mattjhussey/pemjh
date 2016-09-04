""" Tests for challenge17 """
from robber import expect
from pemjh.challenge17 import main


def test_challenge17():
    """ Regression testing challenge17 """
    expect(main(1)).to.eq(None)


def test_challenge17_example():
    expect(main(2)).to.eq(None)
