""" Tests for challenge26 """
from robber import expect
from pemjh.challenge26 import main


def test_challenge26():
    """ Regression testing challenge26 """
    expect(main(1)).to.eq(None)


def test_challenge26_example():
    expect(main(2)).to.eq(None)
