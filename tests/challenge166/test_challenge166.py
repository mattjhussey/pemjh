""" Tests for challenge166 """
from robber import expect
from pemjh.challenge166 import main


def test_challenge166():
    """ Regression testing challenge166 """
    expect(main(1)).to.eq(None)


def test_challenge166_example():
    expect(main(2)).to.eq(None)
