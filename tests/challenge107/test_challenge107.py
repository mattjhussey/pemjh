""" Tests for challenge107 """
from robber import expect
from pemjh.challenge107 import main


def test_challenge107():
    """ Regression testing challenge107 """
    expect(main(1)).to.eq(None)


def test_challenge107_example():
    expect(main(2)).to.eq(None)
