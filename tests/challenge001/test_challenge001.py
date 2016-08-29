""" Tests for challenge001 """
from robber import expect
from pemjh.challenge001 import main


def test_challenge001():
    """ Regression testing challenge001 """
    expect(main(1000)).to.eq(233168)


def test_challenge001_example():
    expect(main(10)).to.eq(23)
