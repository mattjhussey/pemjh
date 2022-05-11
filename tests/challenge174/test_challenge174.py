""" Tests for challenge174 """
import pytest
from robber import expect
from pemjh.challenge174 import main



def test_challenge174():
    """ Regression testing challenge174 """
    expect(main()).to.eq(209566)
