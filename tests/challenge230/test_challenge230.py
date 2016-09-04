""" Tests for challenge230 """
from robber import expect
from pemjh.challenge230 import main


def test_challenge230():
    """ Regression testing challenge230 """
    expect(main(1)).to.eq(None)


def test_challenge230_example():
    expect(main(2)).to.eq(None)
