""" Tests for challenge100 """
from robber import expect
from pemjh.challenge100 import main


def test_challenge100():
    """ Regression testing challenge100 """
    expect(main(1)).to.eq(None)


def test_challenge100_example():
    expect(main(2)).to.eq(None)
