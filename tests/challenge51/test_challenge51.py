""" Tests for challenge51 """
import pytest
from robber import expect
from pemjh.challenge51 import main



def test_challenge51():
    """ Regression testing challenge51 """
    expect(main()).to.eq(121313)
