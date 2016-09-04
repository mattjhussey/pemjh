""" Tests for challenge128 """
from robber import expect
from pemjh.challenge128 import main


def test_challenge128():
    """ Regression testing challenge128 """
    expect(main(1)).to.eq(None)


def test_challenge128_example():
    expect(main(2)).to.eq(None)
