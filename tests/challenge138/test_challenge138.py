""" Tests for challenge138 """
from robber import expect
from pemjh.challenge138 import main


def test_challenge138():
    """ Regression testing challenge138 """
    expect(main()).to.eq(1118049290473932)
