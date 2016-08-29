""" Tests for challenge003 """
from robber import expect
from pemjh.challenge003 import main


def test_challenge003():
    """ Regression testing challenge003 """
    expect(main(600851475143)).to.eq(6857)


def test_challenge003_example():
    expect(main(13195)).to.eq(29)
