""" Tests for challenge94 """
from robber import expect
from pemjh.challenge94 import main


def test_challenge94():
    """ Regression testing challenge94 """
    expect(main()).to.eq(518408346)
