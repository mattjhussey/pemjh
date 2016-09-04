""" Tests for challenge121 """
from robber import expect
from pemjh.challenge121 import main


def test_challenge121():
    """ Regression testing challenge121 """
    expect(main(1)).to.eq(None)


def test_challenge121_example():
    expect(main(2)).to.eq(None)
