""" Tests for challenge12 """
from robber import expect
from pemjh.challenge12 import main


def test_challenge12():
    """ Regression testing challenge12 """
    expect(main(1)).to.eq(None)


def test_challenge12_example():
    expect(main(2)).to.eq(None)
