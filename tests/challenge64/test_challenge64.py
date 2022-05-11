""" Tests for challenge64 """
import pytest
from robber import expect
from pemjh.challenge64 import main



def test_challenge64():
    """ Regression testing challenge64 """
    expect(main()).to.eq(1322)
