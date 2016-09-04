""" Tests for challenge139 """
from robber import expect
from pemjh.challenge139 import main


def test_challenge139():
    """ Regression testing challenge139 """
    expect(main(1)).to.eq(None)


def test_challenge139_example():
    expect(main(2)).to.eq(None)
