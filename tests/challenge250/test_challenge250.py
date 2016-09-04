""" Tests for challenge250 """
from robber import expect
from pemjh.challenge250 import main


def test_challenge250():
    """ Regression testing challenge250 """
    expect(main(1)).to.eq(None)


def test_challenge250_example():
    expect(main(2)).to.eq(None)
