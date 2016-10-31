""" Tests for challenge265 """
from robber import expect
from pemjh.challenge265 import main


def test_challenge265():
    """ Regression testing challenge265 """
    expect(main()).to.eq(209110240768)
