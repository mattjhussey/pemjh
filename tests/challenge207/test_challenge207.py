""" Tests for challenge207 """
from robber import expect
from pemjh.challenge207 import main


def test_challenge207():
    """ Regression testing challenge207 """
    expect(main(1)).to.eq(None)


def test_challenge207_example():
    expect(main(2)).to.eq(None)
