""" Tests for challenge50 """
from robber import expect
from pemjh.challenge50 import main


def test_challenge50():
    """ Regression testing challenge50 """
    expect(main()).to.eq(997651)
