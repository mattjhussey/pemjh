""" Tests for challenge101 """
from robber import expect
from pemjh.challenge101 import main


def test_challenge101():
    """ Regression testing challenge101 """
    expect(main()).to.eq(37076114526)
