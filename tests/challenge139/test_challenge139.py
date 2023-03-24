""" Tests for challenge139 """
from robber import expect
from pemjh.challenge139 import main


def test_challenge139():
    """ Regression testing challenge139 """
    expect(main()).to.eq(10057761)
