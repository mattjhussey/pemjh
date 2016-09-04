""" Tests for challenge94 """
from robber import expect
from pemjh.challenge94 import main


def test_challenge94():
    """ Regression testing challenge94 """
    expect(main(1)).to.eq(None)


def test_challenge94_example():
    expect(main(2)).to.eq(None)
