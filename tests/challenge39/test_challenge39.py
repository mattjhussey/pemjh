""" Tests for challenge39 """
from robber import expect
from pemjh.challenge39 import main


def test_challenge39():
    """ Regression testing challenge39 """
    expect(main(1)).to.eq(None)


def test_challenge39_example():
    expect(main(2)).to.eq(None)
