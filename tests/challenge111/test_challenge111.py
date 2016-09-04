""" Tests for challenge111 """
from robber import expect
from pemjh.challenge111 import main


def test_challenge111():
    """ Regression testing challenge111 """
    expect(main(1)).to.eq(None)


def test_challenge111_example():
    expect(main(2)).to.eq(None)
