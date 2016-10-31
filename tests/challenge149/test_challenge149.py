""" Tests for challenge149 """
from robber import expect
from pemjh.challenge149 import main


def test_challenge149():
    """ Regression testing challenge149 """
    expect(main()).to.eq(52852124)
