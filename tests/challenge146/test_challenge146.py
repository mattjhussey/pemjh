""" Tests for challenge146 """
from robber import expect
from pemjh.challenge146 import main


def test_challenge146():
    """ Regression testing challenge146 """
    expect(main(1)).to.eq(None)


def test_challenge146_example():
    expect(main(2)).to.eq(None)
