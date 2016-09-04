""" Tests for challenge84 """
from robber import expect
from pemjh.challenge84 import main


def test_challenge84():
    """ Regression testing challenge84 """
    expect(main(1)).to.eq(None)


def test_challenge84_example():
    expect(main(2)).to.eq(None)
