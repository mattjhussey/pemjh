""" Tests for challenge17 """
from robber import expect
from pemjh.challenge17 import main


def test_challenge17():
    """ Regression testing challenge17 """
    expect(main()).to.eq(21124)
