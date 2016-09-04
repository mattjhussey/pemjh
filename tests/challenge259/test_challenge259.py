""" Tests for challenge259 """
from robber import expect
from pemjh.challenge259 import main


def test_challenge259():
    """ Regression testing challenge259 """
    expect(main(1)).to.eq(None)


def test_challenge259_example():
    expect(main(2)).to.eq(None)
