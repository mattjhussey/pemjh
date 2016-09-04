""" Tests for challenge133 """
from robber import expect
from pemjh.challenge133 import main


def test_challenge133():
    """ Regression testing challenge133 """
    expect(main(1)).to.eq(None)


def test_challenge133_example():
    expect(main(2)).to.eq(None)
