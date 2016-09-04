""" Tests for challenge19 """
from robber import expect
from pemjh.challenge19 import main


def test_challenge19():
    """ Regression testing challenge19 """
    expect(main(1)).to.eq(None)


def test_challenge19_example():
    expect(main(2)).to.eq(None)
