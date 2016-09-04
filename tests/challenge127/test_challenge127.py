""" Tests for challenge127 """
from robber import expect
from pemjh.challenge127 import main


def test_challenge127():
    """ Regression testing challenge127 """
    expect(main(1)).to.eq(None)


def test_challenge127_example():
    expect(main(2)).to.eq(None)
