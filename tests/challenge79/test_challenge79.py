""" Tests for challenge79 """
from robber import expect
from pemjh.challenge79 import main


def test_challenge79():
    """ Regression testing challenge79 """
    expect(main()).to.eq(73162890)
