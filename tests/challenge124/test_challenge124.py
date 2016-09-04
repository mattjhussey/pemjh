""" Tests for challenge124 """
from robber import expect
from pemjh.challenge124 import main


def test_challenge124():
    """ Regression testing challenge124 """
    expect(main(1)).to.eq(None)


def test_challenge124_example():
    expect(main(2)).to.eq(None)
