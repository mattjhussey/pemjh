""" Tests for challenge214 """
from robber import expect
from pemjh.challenge214 import main


def test_challenge214():
    """ Regression testing challenge214 """
    expect(main(1)).to.eq(None)


def test_challenge214_example():
    expect(main(2)).to.eq(None)
