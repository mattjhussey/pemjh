""" Tests for challenge78 """
from robber import expect
from pemjh.challenge78 import main


def test_challenge78():
    """ Regression testing challenge78 """
    expect(main()).to.eq(55374)
