""" Tests for challenge74 """
import pytest
from robber import expect
from pemjh.challenge74 import main



def test_challenge74():
    """ Regression testing challenge74 """
    expect(main()).to.eq(402)
