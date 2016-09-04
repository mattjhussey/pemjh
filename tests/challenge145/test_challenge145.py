""" Tests for challenge145 """
from robber import expect
from pemjh.challenge145 import main


def test_challenge145():
    """ Regression testing challenge145 """
    expect(main(1)).to.eq(None)


def test_challenge145_example():
    expect(main(2)).to.eq(None)
