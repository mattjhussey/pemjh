""" Tests for challenge43 """
from robber import expect
from pemjh.challenge43 import main


def test_challenge43():
    """ Regression testing challenge43 """
    expect(main(1)).to.eq(None)


def test_challenge43_example():
    expect(main(2)).to.eq(None)
