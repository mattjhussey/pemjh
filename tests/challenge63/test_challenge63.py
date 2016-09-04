""" Tests for challenge63 """
from robber import expect
from pemjh.challenge63 import main


def test_challenge63():
    """ Regression testing challenge63 """
    expect(main(1)).to.eq(None)


def test_challenge63_example():
    expect(main(2)).to.eq(None)
