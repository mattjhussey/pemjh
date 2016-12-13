""" Tests for challenge130 """
import pytest
from robber import expect
from pemjh.challenge130 import main


@pytest.mark.regression
def test_challenge130():
    """ Regression testing challenge130 """
    expect(main()).to.eq(149253)
