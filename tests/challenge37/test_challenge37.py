""" Tests for challenge37 """
from robber import expect
from pemjh.challenge37 import main


def test_challenge37():
    """ Regression testing challenge37 """
    expect(main(1)).to.eq(None)


def test_challenge37_example():
    expect(main(2)).to.eq(None)
