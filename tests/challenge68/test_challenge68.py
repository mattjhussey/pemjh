""" Tests for challenge68 """
from robber import expect
from pemjh.challenge68 import main


def test_challenge68():
    """ Regression testing challenge68 """
    expect(main(1)).to.eq(None)


def test_challenge68_example():
    expect(main(2)).to.eq(None)
