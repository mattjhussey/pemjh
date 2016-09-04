""" Tests for challenge41 """
from robber import expect
from pemjh.challenge41 import main


def test_challenge41():
    """ Regression testing challenge41 """
    expect(main(1)).to.eq(None)


def test_challenge41_example():
    expect(main(2)).to.eq(None)
