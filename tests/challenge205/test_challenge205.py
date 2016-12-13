""" Tests for challenge205 """
import pytest
from robber import expect
from pemjh.challenge205 import main


@pytest.mark.regression
def test_challenge205():
    """ Regression testing challenge205 """
    expect(main()).to.eq(0.5731441)
