""" Tests for challenge115 """
from robber import expect
from pemjh.challenge115 import main


def test_challenge115():
    """ Regression testing challenge115 """
    expect(main(1)).to.eq(None)


def test_challenge115_example():
    expect(main(2)).to.eq(None)
