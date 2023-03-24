""" Tests for challenge162 """
from robber import expect
from pemjh.challenge162 import main


def test_challenge162():
    """ Regression testing challenge162 """
    expect(main()).to.eq('3D58725572C62302')
