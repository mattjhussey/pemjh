""" Tests for challenge148 """
from robber import expect
from pemjh.challenge148 import main


def test_challenge148():
    """ Regression testing challenge148 """
    expect(main(1)).to.eq(None)


def test_challenge148_example():
    expect(main(2)).to.eq(None)
