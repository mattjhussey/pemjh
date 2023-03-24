""" Tests for challenge25 """
from robber import expect
from pemjh.challenge25 import main


def test_challenge25():
    """ Regression testing challenge25 """
    expect(main()).to.eq(4782)
