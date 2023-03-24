""" Tests for challenge106 """
from robber import expect
from pemjh.challenge106 import main


def test_challenge106():
    """ Regression testing challenge106 """
    expect(main()).to.eq(21384)
