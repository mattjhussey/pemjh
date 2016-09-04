""" Tests for challenge190 """
from robber import expect
from pemjh.challenge190 import main


def test_challenge190():
    """ Regression testing challenge190 """
    expect(main(1)).to.eq(None)


def test_challenge190_example():
    expect(main(2)).to.eq(None)
