""" Tests for challenge122 """
from robber import expect
from pemjh.challenge122 import main


def test_challenge122():
    """ Regression testing challenge122 """
    expect(main()).to.eq(1582)
