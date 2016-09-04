""" Tests for challenge83 """
from robber import expect
from pemjh.challenge83 import main


def test_challenge83():
    """ Regression testing challenge83 """
    expect(main(1)).to.eq(None)


def test_challenge83_example():
    expect(main(2)).to.eq(None)
