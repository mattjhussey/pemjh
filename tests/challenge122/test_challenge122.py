""" Tests for challenge122 """
from robber import expect
from pemjh.challenge122 import main


def test_challenge122():
    """ Regression testing challenge122 """
    expect(main(1)).to.eq(None)


def test_challenge122_example():
    expect(main(2)).to.eq(None)
