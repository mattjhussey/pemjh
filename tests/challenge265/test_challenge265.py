""" Tests for challenge265 """
from robber import expect
from pemjh.challenge265 import main


def test_challenge265():
    """ Regression testing challenge265 """
    expect(main(1)).to.eq(None)


def test_challenge265_example():
    expect(main(2)).to.eq(None)
