""" Tests for challenge203 """
from robber import expect
from pemjh.challenge203 import main


def test_challenge203():
    """ Regression testing challenge203 """
    expect(main(1)).to.eq(None)


def test_challenge203_example():
    expect(main(2)).to.eq(None)
