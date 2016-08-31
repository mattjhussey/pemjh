""" Tests for challenge2 """
from robber import expect
from pemjh.challenge2 import main


def test_challenge2():
    """ Regression testing challenge2 """
    expect(main(4000000)).to.eq(4613732)


def test_challenge2_example():
    expect(main(100)).to.eq(44)
