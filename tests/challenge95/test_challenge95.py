""" Tests for challenge95 """
from robber import expect
from pemjh.challenge95 import main


def test_challenge95():
    """ Regression testing challenge95 """
    expect(main()).to.eq(14316)
