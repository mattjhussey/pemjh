""" Tests for challenge118 """
import pytest
from robber import expect
from pemjh.challenge118 import main



def test_challenge118():
    """ Regression testing challenge118 """
    expect(main()).to.eq(44680)
