""" Tests for challenge197 """
import pytest
from robber import expect
from pemjh.challenge197 import main



def test_challenge197():
    """ Regression testing challenge197 """
    expect(main()).to.eq(1.710637717)
