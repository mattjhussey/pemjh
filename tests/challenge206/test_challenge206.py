""" Tests for challenge206 """
from robber import expect
from pemjh.challenge206 import main


def test_challenge206():
    """ Regression testing challenge206 """
    expect(main(1)).to.eq(None)


def test_challenge206_example():
    expect(main(2)).to.eq(None)
