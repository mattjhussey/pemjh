""" Tests for challenge215 """
from robber import expect
from pemjh.challenge215 import main


def test_challenge215():
    """ Regression testing challenge215 """
    expect(main(1)).to.eq(None)


def test_challenge215_example():
    expect(main(2)).to.eq(None)
