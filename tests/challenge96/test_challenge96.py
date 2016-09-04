""" Tests for challenge96 """
from robber import expect
from pemjh.challenge96 import main


def test_challenge96():
    """ Regression testing challenge96 """
    expect(main(1)).to.eq(None)


def test_challenge96_example():
    expect(main(2)).to.eq(None)
