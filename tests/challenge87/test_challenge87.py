""" Tests for challenge87 """
from robber import expect
from pemjh.challenge87 import main


def test_challenge87():
    """ Regression testing challenge87 """
    expect(main(50000000)).to.eq(1097343)


def test_challenge87_example():
    expect(main(50)).to.eq(4)
