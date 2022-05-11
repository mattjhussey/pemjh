""" Tests for challenge173 """
import pytest
from robber import expect
from pemjh.challenge173 import main



def test_challenge173():
    """ Regression testing challenge173 """
    expect(main()).to.eq(1572729)
