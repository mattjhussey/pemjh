""" Tests for challenge81 """
from robber import expect
from pemjh.challenge81 import main


def test_challenge81():
    """ Regression testing challenge81 """
    expect(main(1)).to.eq(None)


def test_challenge81_example():
    expect(main(2)).to.eq(None)
