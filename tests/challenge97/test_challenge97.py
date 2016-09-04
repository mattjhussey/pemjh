""" Tests for challenge97 """
from robber import expect
from pemjh.challenge97 import main


def test_challenge97():
    """ Regression testing challenge97 """
    expect(main(1)).to.eq(None)


def test_challenge97_example():
    expect(main(2)).to.eq(None)
