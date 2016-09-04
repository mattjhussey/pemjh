""" Tests for challenge132 """
from robber import expect
from pemjh.challenge132 import main


def test_challenge132():
    """ Regression testing challenge132 """
    expect(main(1)).to.eq(None)


def test_challenge132_example():
    expect(main(2)).to.eq(None)
