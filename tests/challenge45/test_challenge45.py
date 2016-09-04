""" Tests for challenge45 """
from robber import expect
from pemjh.challenge45 import main


def test_challenge45():
    """ Regression testing challenge45 """
    expect(main(1)).to.eq(None)


def test_challenge45_example():
    expect(main(2)).to.eq(None)
