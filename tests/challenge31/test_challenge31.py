""" Tests for challenge31 """
from robber import expect
from pemjh.challenge31 import main


def test_challenge31():
    """ Regression testing challenge31 """
    expect(main()).to.eq(73682)
