""" Tests for challenge92 """
from robber import expect
from pemjh.challenge92 import main


def test_challenge92():
    """ Regression testing challenge92 """
    expect(main()).to.eq(8581146)
