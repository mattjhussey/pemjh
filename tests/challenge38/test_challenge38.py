""" Tests for challenge38 """
from robber import expect
from pemjh.challenge38 import main


def test_challenge38():
    """ Regression testing challenge38 """
    expect(main(1)).to.eq(None)


def test_challenge38_example():
    expect(main(2)).to.eq(None)
