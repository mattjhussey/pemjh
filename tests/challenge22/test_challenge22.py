""" Tests for challenge22 """
from robber import expect
from pemjh.challenge22 import main


def test_challenge22():
    """ Regression testing challenge22 """
    expect(main(1)).to.eq(None)


def test_challenge22_example():
    expect(main(2)).to.eq(None)
