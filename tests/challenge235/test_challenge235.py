""" Tests for challenge235 """
from robber import expect
from pemjh.challenge235 import main


def test_challenge235():
    """ Regression testing challenge235 """
    expect(main(1)).to.eq(None)


def test_challenge235_example():
    expect(main(2)).to.eq(None)
