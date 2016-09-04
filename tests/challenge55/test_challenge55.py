""" Tests for challenge55 """
from robber import expect
from pemjh.challenge55 import main


def test_challenge55():
    """ Regression testing challenge55 """
    expect(main(1)).to.eq(None)


def test_challenge55_example():
    expect(main(2)).to.eq(None)
