""" Tests for challenge187 """
import pytest
from robber import expect
from pemjh.challenge187 import main



def test_challenge187():
    """ Regression testing challenge187 """
    expect(main()).to.eq(17427258)
