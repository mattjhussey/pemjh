""" Tests for challenge58 """
import pytest
from robber import expect
from pemjh.challenge58 import main



def test_challenge58():
    """ Regression testing challenge58 """
    expect(main()).to.eq(26241)
