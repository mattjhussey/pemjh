""" Tests for challenge67 """
from robber import expect
from pemjh.challenge67 import main


def test_challenge67():
    """ Regression testing challenge67 """
    expect(main(1)).to.eq(None)


def test_challenge67_example():
    expect(main(2)).to.eq(None)
