""" Tests for challenge162 """
from robber import expect
from pemjh.challenge162 import main


def test_challenge162():
    """ Regression testing challenge162 """
    expect(main(1)).to.eq(None)


def test_challenge162_example():
    expect(main(2)).to.eq(None)
