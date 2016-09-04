""" Tests for challenge220 """
from robber import expect
from pemjh.challenge220 import main


def test_challenge220():
    """ Regression testing challenge220 """
    expect(main(1)).to.eq(None)


def test_challenge220_example():
    expect(main(2)).to.eq(None)
