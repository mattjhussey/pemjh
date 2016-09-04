""" Tests for challenge134 """
from robber import expect
from pemjh.challenge134 import main


def test_challenge134():
    """ Regression testing challenge134 """
    expect(main(1)).to.eq(None)


def test_challenge134_example():
    expect(main(2)).to.eq(None)
