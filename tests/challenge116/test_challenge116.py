""" Tests for challenge116 """
from robber import expect
from pemjh.challenge116 import main


def test_challenge116():
    """ Regression testing challenge116 """
    expect(main(1)).to.eq(None)


def test_challenge116_example():
    expect(main(2)).to.eq(None)
