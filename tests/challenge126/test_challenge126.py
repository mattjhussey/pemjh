""" Tests for challenge126 """
from robber import expect
from pemjh.challenge126 import main


def test_challenge126():
    """ Regression testing challenge126 """
    expect(main(1)).to.eq(None)


def test_challenge126_example():
    expect(main(2)).to.eq(None)
