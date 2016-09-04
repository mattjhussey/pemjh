""" Tests for challenge225 """
from robber import expect
from pemjh.challenge225 import main


def test_challenge225():
    """ Regression testing challenge225 """
    expect(main(1)).to.eq(None)


def test_challenge225_example():
    expect(main(2)).to.eq(None)
