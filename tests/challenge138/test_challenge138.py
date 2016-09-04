""" Tests for challenge138 """
from robber import expect
from pemjh.challenge138 import main


def test_challenge138():
    """ Regression testing challenge138 """
    expect(main(1)).to.eq(None)


def test_challenge138_example():
    expect(main(2)).to.eq(None)
