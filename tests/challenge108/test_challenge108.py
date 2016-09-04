""" Tests for challenge108 """
from robber import expect
from pemjh.challenge108 import main


def test_challenge108():
    """ Regression testing challenge108 """
    expect(main(1)).to.eq(None)


def test_challenge108_example():
    expect(main(2)).to.eq(None)
