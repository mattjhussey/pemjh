""" Tests for challenge65 """
from robber import expect
from pemjh.challenge65 import main


def test_challenge65():
    """ Regression testing challenge65 """
    expect(main()).to.eq(272)
