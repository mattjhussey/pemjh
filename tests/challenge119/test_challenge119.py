""" Tests for challenge119 """
from robber import expect
from pemjh.challenge119 import main


def test_challenge119():
    """ Regression testing challenge119 """
    expect(main(1)).to.eq(None)


def test_challenge119_example():
    expect(main(2)).to.eq(None)
