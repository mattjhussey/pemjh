""" Tests for challenge114 """
from robber import expect
from pemjh.challenge114 import main


def test_challenge114():
    """ Regression testing challenge114 """
    expect(main(1)).to.eq(None)


def test_challenge114_example():
    expect(main(2)).to.eq(None)
