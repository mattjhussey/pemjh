""" Tests for challenge164 """
from robber import expect
from pemjh.challenge164 import main


def test_challenge164():
    """ Regression testing challenge164 """
    expect(main(1)).to.eq(None)


def test_challenge164_example():
    expect(main(2)).to.eq(None)
