""" Tests for challenge99 """
from robber import expect
from pemjh.challenge99 import main


def test_challenge99():
    """ Regression testing challenge99 """
    expect(main(1)).to.eq(None)


def test_challenge99_example():
    expect(main(2)).to.eq(None)
