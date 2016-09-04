""" Tests for challenge47 """
from robber import expect
from pemjh.challenge47 import main


def test_challenge47():
    """ Regression testing challenge47 """
    expect(main(1)).to.eq(None)


def test_challenge47_example():
    expect(main(2)).to.eq(None)
