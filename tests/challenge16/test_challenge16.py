""" Tests for challenge16 """
from robber import expect
from pemjh.challenge16 import main


def test_challenge16():
    """ Regression testing challenge16 """
    expect(main(1)).to.eq(None)


def test_challenge16_example():
    expect(main(2)).to.eq(None)
