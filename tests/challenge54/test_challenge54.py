""" Tests for challenge54 """
from robber import expect
from pemjh.challenge54 import main


def test_challenge54():
    """ Regression testing challenge54 """
    expect(main(1)).to.eq(None)


def test_challenge54_example():
    expect(main(2)).to.eq(None)
