""" Tests for challenge132 """
from robber import expect
from pemjh.challenge132 import main


def test_challenge132():
    """ Regression testing challenge132 """
    expect(main()).to.eq(843296)
