""" Tests for challenge29 """
from robber import expect
from pemjh.challenge29 import main


def test_challenge29():
    """ Regression testing challenge29 """
    expect(main()).to.eq(9183)
