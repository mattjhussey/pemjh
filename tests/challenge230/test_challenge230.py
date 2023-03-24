""" Tests for challenge230 """
from robber import expect
from pemjh.challenge230 import main


def test_challenge230():
    """ Regression testing challenge230 """
    expect(main()).to.eq(850481152593119296)
