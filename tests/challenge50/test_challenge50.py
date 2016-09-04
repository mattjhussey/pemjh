""" Tests for challenge50 """
from robber import expect
from pemjh.challenge50 import main


def test_challenge50():
    """ Regression testing challenge50 """
    expect(main(1)).to.eq(None)


def test_challenge50_example():
    expect(main(2)).to.eq(None)
