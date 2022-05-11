""" Tests for challenge33 """
import pytest
from robber import expect
from pemjh.challenge33 import main



def test_challenge33():
    """ Regression testing challenge33 """
    expect(main()).to.eq(100)
