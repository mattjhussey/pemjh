""" Tests for challenge13 """
from robber import expect
from pemjh.challenge13 import main


def test_challenge13():
    """ Regression testing challenge13 """
    expect(main()).to.eq(5537376230)
