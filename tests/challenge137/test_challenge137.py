""" Tests for challenge137 """
from robber import expect
from pemjh.challenge137 import main


def test_challenge137():
    """ Regression testing challenge137 """
    expect(main(1)).to.eq(None)


def test_challenge137_example():
    expect(main(2)).to.eq(None)
