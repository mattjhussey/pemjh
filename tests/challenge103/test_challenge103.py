""" Tests for challenge103 """
from robber import expect
from pemjh.challenge103 import main


def test_challenge103():
    """ Regression testing challenge103 """
    expect(main(1)).to.eq(None)


def test_challenge103_example():
    expect(main(2)).to.eq(None)
