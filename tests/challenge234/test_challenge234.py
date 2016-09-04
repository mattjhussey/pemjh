""" Tests for challenge234 """
from robber import expect
from pemjh.challenge234 import main


def test_challenge234():
    """ Regression testing challenge234 """
    expect(main(1)).to.eq(None)


def test_challenge234_example():
    expect(main(2)).to.eq(None)
