""" Tests for challenge53 """
import pytest
from robber import expect
from pemjh.challenge53 import main



def test_challenge53():
    """ Regression testing challenge53 """
    expect(main()).to.eq(4075)
