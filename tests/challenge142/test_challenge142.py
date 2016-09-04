""" Tests for challenge142 """
from robber import expect
from pemjh.challenge142 import main


def test_challenge142():
    """ Regression testing challenge142 """
    expect(main(1)).to.eq(None)


def test_challenge142_example():
    expect(main(2)).to.eq(None)
