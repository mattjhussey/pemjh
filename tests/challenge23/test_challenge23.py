""" Tests for challenge23 """
from robber import expect
from pemjh.challenge23 import main


def test_challenge23():
    """ Regression testing challenge23 """
    expect(main(1)).to.eq(None)


def test_challenge23_example():
    expect(main(2)).to.eq(None)
