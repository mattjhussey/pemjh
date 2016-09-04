""" Tests for challenge197 """
from robber import expect
from pemjh.challenge197 import main


def test_challenge197():
    """ Regression testing challenge197 """
    expect(main(1)).to.eq(None)


def test_challenge197_example():
    expect(main(2)).to.eq(None)
