""" Tests for challenge250 """
from robber import expect
from pemjh.challenge250 import main


def test_challenge250():
    """ Regression testing challenge250 """
    expect(main()).to.eq(1425480602091519)
