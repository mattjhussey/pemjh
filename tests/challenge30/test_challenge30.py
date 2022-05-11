""" Tests for challenge30 """
import pytest
from robber import expect
from pemjh.challenge30 import main



def test_challenge30():
    """ Regression testing challenge30 """
    expect(main()).to.eq(443839)
