""" Tests for challenge129 """
from robber import expect
from pemjh.challenge129 import main


def test_challenge129():
    """ Regression testing challenge129 """
    expect(main(1)).to.eq(None)


def test_challenge129_example():
    expect(main(2)).to.eq(None)
