""" Tests for challenge39 """
import pytest
from robber import expect
from pemjh.challenge39 import main



def test_challenge39():
    """ Regression testing challenge39 """
    expect(main()).to.eq(840)
