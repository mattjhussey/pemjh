""" Tests for challenge144 """
import pytest
from robber import expect
from pemjh.challenge144 import main



def test_challenge144():
    """ Regression testing challenge144 """
    expect(main()).to.eq(354)
