""" Tests for challenge104 """
from robber import expect
from pemjh.challenge104 import main


def test_challenge104():
    """ Regression testing challenge104 """
    expect(main(1)).to.eq(None)


def test_challenge104_example():
    expect(main(2)).to.eq(None)
