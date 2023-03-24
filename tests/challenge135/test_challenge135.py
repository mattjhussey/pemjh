""" Tests for challenge135 """
from robber import expect
from pemjh.challenge135 import main


def test_challenge135():
    """ Regression testing challenge135 """
    expect(main()).to.eq(4989)
