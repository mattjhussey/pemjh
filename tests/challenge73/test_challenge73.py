""" Tests for challenge73 """
import pytest
from robber import expect
from pemjh.challenge73 import main



def test_challenge73():
    """ Regression testing challenge73 """
    expect(main()).to.eq(7295372)
