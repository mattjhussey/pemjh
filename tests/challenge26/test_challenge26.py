""" Tests for challenge26 """
import pytest
from robber import expect
from pemjh.challenge26 import main



def test_challenge26():
    """ Regression testing challenge26 """
    expect(main()).to.eq(983)
