""" Tests for challenge174 """
from robber import expect
from pemjh.challenge174 import main


def test_challenge174():
    """ Regression testing challenge174 """
    expect(main(1)).to.eq(None)


def test_challenge174_example():
    expect(main(2)).to.eq(None)
