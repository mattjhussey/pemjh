""" Tests for challenge40 """
from robber import expect
from pemjh.challenge40 import main


def test_challenge40():
    """ Regression testing challenge40 """
    expect(main()).to.eq(210)
