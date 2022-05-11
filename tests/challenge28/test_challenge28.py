""" Tests for challenge28 """
import pytest
from robber import expect
from pemjh.challenge28 import main



def test_challenge28():
    """ Regression testing challenge28 """
    expect(main()).to.eq(669171001)
