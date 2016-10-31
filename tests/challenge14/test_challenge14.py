""" Tests for challenge14 """
from robber import expect
from pemjh.challenge14 import main


def test_challenge14():
    """ Regression testing challenge14 """
    expect(main()).to.eq(837799)
