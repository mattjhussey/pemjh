""" Tests for challenge117 """
from robber import expect
from pemjh.challenge117 import main


def test_challenge117():
    """ Regression testing challenge117 """
    expect(main(1)).to.eq(None)


def test_challenge117_example():
    expect(main(2)).to.eq(None)
