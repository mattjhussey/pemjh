""" Tests for challenge243 """
import pytest
from robber import expect
from pemjh.challenge243 import main


def test_challenge243():
    """ Regression testing challenge243 """
    expect(main()).to.eq(892371480)
