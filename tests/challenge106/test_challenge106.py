""" Tests for challenge106 """
from robber import expect
from pemjh.challenge106 import main


def test_challenge106():
    """ Regression testing challenge106 """
    expect(main(1)).to.eq(None)


def test_challenge106_example():
    expect(main(2)).to.eq(None)
