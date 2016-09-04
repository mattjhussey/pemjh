""" Tests for challenge69 """
from robber import expect
from pemjh.challenge69 import main


def test_challenge69():
    """ Regression testing challenge69 """
    expect(main(1)).to.eq(None)


def test_challenge69_example():
    expect(main(2)).to.eq(None)
