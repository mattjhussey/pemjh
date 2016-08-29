""" Tests for challenge002 """
from robber import expect
from pemjh.challenge002 import main


def test_challenge002():
    """ Regression testing challenge002 """
    expect(main(4000000)).to.eq(4613732)


def test_challenge002_example():
    expect(main(100)).to.eq(44)
