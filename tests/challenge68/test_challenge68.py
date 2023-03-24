""" Tests for challenge68 """
from robber import expect
from pemjh.challenge68 import main


def test_challenge68():
    """ Regression testing challenge68 """
    expect(main()).to.eq(6531031914842725)
