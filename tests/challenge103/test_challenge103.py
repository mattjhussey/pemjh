""" Tests for challenge103 """
from robber import expect
from pemjh.challenge103 import main


def test_challenge103():
    """ Regression testing challenge103 """
    expect(main()).to.eq(20313839404245)
