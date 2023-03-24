""" Tests for challenge179 """
from robber import expect
from pemjh.challenge179 import main


def test_challenge179():
    """ Regression testing challenge179 """
    expect(main()).to.eq(986262)
