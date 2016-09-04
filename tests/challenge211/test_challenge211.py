""" Tests for challenge211 """
from robber import expect
from pemjh.challenge211 import main


def test_challenge211():
    """ Regression testing challenge211 """
    expect(main(1)).to.eq(None)


def test_challenge211_example():
    expect(main(2)).to.eq(None)
