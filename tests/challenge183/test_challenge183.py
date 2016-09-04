""" Tests for challenge183 """
from robber import expect
from pemjh.challenge183 import main


def test_challenge183():
    """ Regression testing challenge183 """
    expect(main(1)).to.eq(None)


def test_challenge183_example():
    expect(main(2)).to.eq(None)
