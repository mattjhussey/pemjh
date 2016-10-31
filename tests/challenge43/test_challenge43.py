""" Tests for challenge43 """
from robber import expect
from pemjh.challenge43 import main


def test_challenge43():
    """ Regression testing challenge43 """
    expect(main()).to.eq(16695334890)
