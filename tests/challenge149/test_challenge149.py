""" Tests for challenge149 """
from robber import expect
from pemjh.challenge149 import main


def test_challenge149():
    """ Regression testing challenge149 """
    expect(main(1)).to.eq(None)


def test_challenge149_example():
    expect(main(2)).to.eq(None)
