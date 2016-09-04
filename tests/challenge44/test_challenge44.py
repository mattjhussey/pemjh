""" Tests for challenge44 """
from robber import expect
from pemjh.challenge44 import main


def test_challenge44():
    """ Regression testing challenge44 """
    expect(main(1)).to.eq(None)


def test_challenge44_example():
    expect(main(2)).to.eq(None)
