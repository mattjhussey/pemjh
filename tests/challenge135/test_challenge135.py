""" Tests for challenge135 """
from robber import expect
from pemjh.challenge135 import main


def test_challenge135():
    """ Regression testing challenge135 """
    expect(main(1)).to.eq(None)


def test_challenge135_example():
    expect(main(2)).to.eq(None)
