""" Tests for challenge25 """
from robber import expect
from pemjh.challenge25 import main


def test_challenge25():
    """ Regression testing challenge25 """
    expect(main(1)).to.eq(None)


def test_challenge25_example():
    expect(main(2)).to.eq(None)
