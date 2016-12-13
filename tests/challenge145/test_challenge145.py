""" Tests for challenge145 """
import pytest
from robber import expect
from pemjh.challenge145 import main


@pytest.mark.regression
def test_challenge145():
    """ Regression testing challenge145 """
    expect(main()).to.eq(608720)
