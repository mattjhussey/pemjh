""" Tests for challenge16 """
import pytest
from robber import expect
from pemjh.challenge16 import main


@pytest.mark.regression
def test_challenge16():
    """ Regression testing challenge16 """
    expect(main()).to.eq(1366)
