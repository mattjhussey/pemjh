""" Tests for challenge191 """
from robber import expect
from pemjh.challenge191 import main


def test_challenge191():
    """ Regression testing challenge191 """
    expect(main(1)).to.eq(None)


def test_challenge191_example():
    expect(main(2)).to.eq(None)
