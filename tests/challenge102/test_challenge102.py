""" Tests for challenge102 """
from robber import expect
from pemjh.challenge102 import main


def test_challenge102():
    """ Regression testing challenge102 """
    expect(main(1)).to.eq(None)


def test_challenge102_example():
    expect(main(2)).to.eq(None)
