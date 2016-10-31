""" Tests for challenge49 """
from robber import expect
from pemjh.challenge49 import main


def test_challenge49():
    """ Regression testing challenge49 """
    expect(main()).to.eq(296962999629)
