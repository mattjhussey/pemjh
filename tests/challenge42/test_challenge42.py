""" Tests for challenge42 """
from robber import expect
from pemjh.challenge42 import main


def test_challenge42():
    """ Regression testing challenge42 """
    expect(main(1)).to.eq(None)


def test_challenge42_example():
    expect(main(2)).to.eq(None)
