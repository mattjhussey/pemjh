""" Tests for challenge133 """
from robber import expect
from pemjh.challenge133 import main


def test_challenge133():
    """ Regression testing challenge133 """
    expect(main()).to.eq(453647705)
