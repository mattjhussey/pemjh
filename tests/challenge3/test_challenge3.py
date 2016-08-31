""" Tests for challenge3 """
from robber import expect
from pemjh.challenge3 import main


def test_challenge3():
    """ Regression testing challenge3 """
    expect(main(600851475143)).to.eq(6857)


def test_challenge3_example():
    expect(main(13195)).to.eq(29)
