""" Tests for challenge203 """
from robber import expect
from pemjh.challenge203 import main


def test_challenge203():
    """ Regression testing challenge203 """
    expect(main()).to.eq(34029210557338)
