""" Tests for challenge78 """
from robber import expect
from pemjh.challenge78 import main


def test_challenge78():
    """ Regression testing challenge78 """
    expect(main(1)).to.eq(None)


def test_challenge78_example():
    expect(main(2)).to.eq(None)
