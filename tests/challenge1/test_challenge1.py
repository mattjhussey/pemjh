""" Tests for challenge1 """
from robber import expect
from pemjh.challenge1 import main


def test_challenge1():
    """ Regression testing challenge1 """
    expect(main(1000)).to.eq(233168)


def test_challenge1_example():
    expect(main(10)).to.eq(23)
