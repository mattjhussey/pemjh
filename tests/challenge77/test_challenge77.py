""" Tests for challenge77 """
import pytest
from robber import expect
from pemjh.challenge77 import main



def test_challenge77():
    """ Regression testing challenge77 """
    expect(main()).to.eq(71)
