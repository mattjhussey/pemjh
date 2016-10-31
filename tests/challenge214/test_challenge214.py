""" Tests for challenge214 """
from robber import expect
from pemjh.challenge214 import main


def test_challenge214():
    """ Regression testing challenge214 """
    expect(main()).to.eq(1677366278943)
