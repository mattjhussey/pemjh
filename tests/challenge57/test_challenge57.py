""" Tests for challenge57 """
from robber import expect
from pemjh.challenge57 import main


def test_challenge57():
    """ Regression testing challenge57 """
    expect(main(1)).to.eq(None)


def test_challenge57_example():
    expect(main(2)).to.eq(None)
