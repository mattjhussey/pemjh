""" Tests for challenge235 """
from robber import expect
from pemjh.challenge235 import main


def test_challenge235():
    """ Regression testing challenge235 """
    expect(main()).to.eq('1.002322108633')
