""" Tests for challenge29 """
from robber import expect
from pemjh.challenge29 import main


def test_challenge29():
    """ Regression testing challenge29 """
    expect(main(1)).to.eq(None)


def test_challenge29_example():
    expect(main(2)).to.eq(None)
