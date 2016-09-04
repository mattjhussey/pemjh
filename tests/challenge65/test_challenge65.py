""" Tests for challenge65 """
from robber import expect
from pemjh.challenge65 import main


def test_challenge65():
    """ Regression testing challenge65 """
    expect(main(1)).to.eq(None)


def test_challenge65_example():
    expect(main(2)).to.eq(None)
