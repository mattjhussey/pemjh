""" Tests for challenge63 """
import pytest
from robber import expect
from pemjh.challenge63 import main



def test_challenge63():
    """ Regression testing challenge63 """
    expect(main()).to.eq(49)
