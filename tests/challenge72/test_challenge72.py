""" Tests for challenge72 """
from robber import expect
from pemjh.challenge72 import main


def test_challenge72():
    """ Regression testing challenge72 """
    expect(main()).to.eq(303963552391)
