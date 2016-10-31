""" Tests for challenge56 """
from robber import expect
from pemjh.challenge56 import main


def test_challenge56():
    """ Regression testing challenge56 """
    expect(main()).to.eq(972)
