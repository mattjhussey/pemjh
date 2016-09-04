""" Tests for challenge95 """
from robber import expect
from pemjh.challenge95 import main


def test_challenge95():
    """ Regression testing challenge95 """
    expect(main(1)).to.eq(None)


def test_challenge95_example():
    expect(main(2)).to.eq(None)
