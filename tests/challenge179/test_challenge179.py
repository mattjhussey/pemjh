""" Tests for challenge179 """
from robber import expect
from pemjh.challenge179 import main


def test_challenge179():
    """ Regression testing challenge179 """
    expect(main(1)).to.eq(None)


def test_challenge179_example():
    expect(main(2)).to.eq(None)
