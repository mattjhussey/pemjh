""" Tests for challenge49 """
from robber import expect
from pemjh.challenge49 import main


def test_challenge49():
    """ Regression testing challenge49 """
    expect(main(1)).to.eq(None)


def test_challenge49_example():
    expect(main(2)).to.eq(None)
