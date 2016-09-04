""" Tests for challenge18 """
from robber import expect
from pemjh.challenge18 import main


def test_challenge18():
    """ Regression testing challenge18 """
    expect(main(1)).to.eq(None)


def test_challenge18_example():
    expect(main(2)).to.eq(None)
