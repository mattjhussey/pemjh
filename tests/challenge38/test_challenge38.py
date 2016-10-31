""" Tests for challenge38 """
from robber import expect
from pemjh.challenge38 import main


def test_challenge38():
    """ Regression testing challenge38 """
    expect(main()).to.eq(932718654)
