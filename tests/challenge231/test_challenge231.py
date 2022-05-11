""" Tests for challenge231 """
import pytest
from robber import expect
from pemjh.challenge231 import main


def test_challenge231():
    """ Regression testing challenge231 """
    expect(main()).to.eq(7526965179680)
