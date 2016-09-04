""" Tests for challenge62 """
from robber import expect
from pemjh.challenge62 import main


def test_challenge62():
    """ Regression testing challenge62 """
    expect(main(1)).to.eq(None)


def test_challenge62_example():
    expect(main(2)).to.eq(None)
