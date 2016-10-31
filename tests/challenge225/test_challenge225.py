""" Tests for challenge225 """
from robber import expect
from pemjh.challenge225 import main


def test_challenge225():
    """ Regression testing challenge225 """
    expect(main()).to.eq(2009)
