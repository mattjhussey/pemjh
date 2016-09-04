""" Tests for challenge59 """
from robber import expect
from pemjh.challenge59 import main


def test_challenge59():
    """ Regression testing challenge59 """
    expect(main(1)).to.eq(None)


def test_challenge59_example():
    expect(main(2)).to.eq(None)
