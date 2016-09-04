""" Tests for challenge123 """
from robber import expect
from pemjh.challenge123 import main


def test_challenge123():
    """ Regression testing challenge123 """
    expect(main(1)).to.eq(None)


def test_challenge123_example():
    expect(main(2)).to.eq(None)
