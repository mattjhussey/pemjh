""" Tests for challenge134 """
import pytest
from robber import expect
from pemjh.challenge134 import main


@pytest.mark.regression
def test_challenge134():
    """ Regression testing challenge134 """
    expect(main()).to.eq(18613426663617118)
