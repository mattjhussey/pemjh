""" Tests for challenge57 """
from robber import expect
from pemjh.challenge57 import main


def test_challenge57():
    """ Regression testing challenge57 """
    expect(main()).to.eq(153)
