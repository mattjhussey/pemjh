""" Tests for challenge56 """
from robber import expect
from pemjh.challenge56 import main


def test_challenge56():
    """ Regression testing challenge56 """
    expect(main(1)).to.eq(None)


def test_challenge56_example():
    expect(main(2)).to.eq(None)
