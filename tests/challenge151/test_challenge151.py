""" Tests for challenge151 """
from robber import expect
from pemjh.challenge151 import main


def test_challenge151():
    """ Regression testing challenge151 """
    expect(main(1)).to.eq(None)


def test_challenge151_example():
    expect(main(2)).to.eq(None)
