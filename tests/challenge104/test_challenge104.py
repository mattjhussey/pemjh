""" Tests for challenge104 """
import pytest
from robber import expect
from pemjh.challenge104 import main



def test_challenge104():
    """ Regression testing challenge104 """
    expect(main()).to.eq(329468)
