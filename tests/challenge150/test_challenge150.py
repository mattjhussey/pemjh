""" Tests for challenge150 """
from robber import expect
from pemjh.challenge150 import main


def test_challenge150():
    """ Regression testing challenge150 """
    expect(main()).to.eq(-271248680)
