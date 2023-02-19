""" Tests for challenge90 """
from robber import expect
from pemjh.challenge90 import main


def test_challenge90():
    """ Regression testing challenge90 """
    expect(main()).to.eq(1217)
