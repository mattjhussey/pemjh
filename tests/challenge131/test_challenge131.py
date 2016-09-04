""" Tests for challenge131 """
from robber import expect
from pemjh.challenge131 import main


def test_challenge131():
    """ Regression testing challenge131 """
    expect(main(1)).to.eq(None)


def test_challenge131_example():
    expect(main(2)).to.eq(None)
