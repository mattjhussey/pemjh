""" Tests for challenge187 """
from robber import expect
from pemjh.challenge187 import main


def test_challenge187():
    """ Regression testing challenge187 """
    expect(main(1)).to.eq(None)


def test_challenge187_example():
    expect(main(2)).to.eq(None)
