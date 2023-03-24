""" Tests for challenge234 """
from robber import expect
from pemjh.challenge234 import main


def test_challenge234():
    """ Regression testing challenge234 """
    expect(main()).to.eq(1259187438574927161)
