""" Tests for challenge40 """
from robber import expect
from pemjh.challenge40 import main


def test_challenge40():
    """ Regression testing challenge40 """
    expect(main(1)).to.eq(None)


def test_challenge40_example():
    expect(main(2)).to.eq(None)
