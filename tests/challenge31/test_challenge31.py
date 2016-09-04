""" Tests for challenge31 """
from robber import expect
from pemjh.challenge31 import main


def test_challenge31():
    """ Regression testing challenge31 """
    expect(main(1)).to.eq(None)


def test_challenge31_example():
    expect(main(2)).to.eq(None)
