""" Tests for challenge66 """
from robber import expect
from pemjh.challenge66 import main


def test_challenge66():
    """ Regression testing challenge66 """
    expect(main(1)).to.eq(None)


def test_challenge66_example():
    expect(main(2)).to.eq(None)
