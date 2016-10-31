""" Tests for challenge215 """
from robber import expect
from pemjh.challenge215 import main


def test_challenge215():
    """ Regression testing challenge215 """
    expect(main()).to.eq(806844323190414)
