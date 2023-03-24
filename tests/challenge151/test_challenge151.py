""" Tests for challenge151 """
from robber import expect
from pemjh.challenge151 import main


def test_challenge151():
    """ Regression testing challenge151 """
    expect(main()).to.eq(0.464399)
